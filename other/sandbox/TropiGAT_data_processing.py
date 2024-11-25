# Utils function for data

import os
import random
import warnings
from collections import Counter
from multiprocessing.pool import ThreadPool
import json
import math
import logging

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import torch.optim as optim
from sklearn.metrics import (accuracy_score, f1_score, matthews_corrcoef,
                             precision_score, recall_score, roc_auc_score)
import optuna
from sklearn.model_selection import StratifiedKFold
from torch import nn
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch_geometric.nn import GATv2Conv, HeteroConv
from tqdm import tqdm

import TropiGAT_graph
import TropiGAT_models

# Set random seed for reproducibility
def set_seed(seed=243):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    
# Constants
PATH_WORK = "/home/conchae/prediction_depolymerase_tropism/prophage_prediction/depolymerase_decipher/ficheros_28032023"

# Data processing
def load_and_preprocess_data():
    """Load and preprocess the prophage data."""
    df_info = pd.read_csv(f"{PATH_WORK}/train_nn/TropiGATv2.final_df_v2.tsv", sep="\t", header=0)
    df_info = df_info.drop_duplicates(subset=["Protein_name"])
    
    df_prophages = df_info.drop_duplicates(subset=["Phage"], keep="first")
    dico_prophage_info = {row["Phage"]: {"prophage_strain": row["prophage_id"], "ancestor": row["Infected_ancestor"]} 
                          for _, row in df_prophages.iterrows()}
    
    return df_info, dico_prophage_info

def filter_prophages(df_info, dico_prophage_info):
    """Filter prophages to remove duplicates and ensure diversity."""
    def get_filtered_prophages(prophage):
        combinations = []
        to_exclude = set()
        to_keep = set()
        to_keep.add(prophage)
        df_prophage_group = df_info[
            (df_info["prophage_id"] == dico_prophage_info[prophage]["prophage_strain"]) & 
            (df_info["Infected_ancestor"] == dico_prophage_info[prophage]["ancestor"])
        ]
        if len(df_prophage_group) == 1:
            return df_prophage_group, to_exclude, to_keep
        
        depo_set = set(df_prophage_group[df_prophage_group["Phage"] == prophage]["domain_seq"].values)
        for prophage_tmp in df_prophage_group["Phage"].unique():
            if prophage_tmp != prophage:
                tmp_depo_set = set(df_prophage_group[df_prophage_group["Phage"] == prophage_tmp]["domain_seq"].values)
                if depo_set == tmp_depo_set:
                    to_exclude.add(prophage_tmp)
                elif tmp_depo_set not in combinations:
                    to_keep.add(prophage_tmp)
                    combinations.append(tmp_depo_set)
                else:
                    to_exclude.add(prophage_tmp)
        return df_prophage_group, to_exclude, to_keep

    good_prophages = set()
    excluded_prophages = set()

    for prophage in tqdm(dico_prophage_info.keys()):
        if prophage not in excluded_prophages and prophage not in good_prophages:
            _, excluded_members, kept_members = get_filtered_prophages(prophage)
            good_prophages.update(kept_members)
            excluded_prophages.update(excluded_members)

    df_info_filtered = df_info[df_info["Phage"].isin(good_prophages)]
    df_info_final = df_info_filtered[~df_info_filtered["KL_type_LCA"].str.contains("\\|")]

    return df_info_final

def ultrafilter_prophages(df_info):
    """Perform ultra-filtration to remove duplicate prophages within KL types."""
    duplicate_prophage = []
    dico_kltype_duplica = {}

    for kltype in df_info["KL_type_LCA"].unique():
        df_kl = df_info[df_info["KL_type_LCA"] == kltype][["Phage", "Protein_name", "KL_type_LCA", "Infected_ancestor", "index", "seq", "domain_seq"]]
        prophages_tmp_list = df_kl["Phage"].unique().tolist()
        set_sets_depo = []
        duplicated = {}  
        for prophage_tmp in prophages_tmp_list: 
            set_depo = frozenset(df_kl[df_kl["Phage"] == prophage_tmp]["domain_seq"].values)
            for past_set in set_sets_depo:
                if past_set == set_depo:
                    duplicated[past_set] = duplicated.get(past_set, 0) + 1
                    duplicate_prophage.append(prophage_tmp)
                    break
            else:
                set_sets_depo.append(set_depo)
                duplicated[set_depo] = 1
        dico_kltype_duplica[kltype] = duplicated

    df_info_ultrafiltered = df_info[~df_info["Phage"].isin(duplicate_prophage)]
    
    if ultrafiltration :
        return df_info_ultrafiltered
    else :
        return df_info

def prepare_kltypes(df_info):
    """Prepare KL types for training."""
    df_prophages = df_info.drop_duplicates(subset=["Phage"])
    dico_prophage_count = dict(Counter(df_prophages["KL_type_LCA"]))
    kltypes = [kltype for kltype, count in dico_prophage_count.items() if count >= 10]
    return kltypes, dico_prophage_count


def log_trial_hyperparameters(trial_number, hyperparameters, log_file):
    """Log the hyperparameters for a specific trial."""
    with open(log_file, 'a') as f:
        f.write(f"Trial {trial_number} Hyperparameters: {json.dumps(hyperparameters)}\n")

        
def log_trial_loss(trial_number, epoch, train_loss, test_loss, log_file):
    """Log the loss for each trial and epoch to a file."""
    with open(log_file, 'a') as f:
        f.write(f"Trial {trial_number}, Epoch {epoch}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}\n")