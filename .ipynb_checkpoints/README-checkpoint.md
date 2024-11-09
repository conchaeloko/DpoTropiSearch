DpoTropiSearch

This repository contains the implementation and data for DpoTropiSearch, a research project aimed at predicting the capsular type-specificity of phage depolymerases targeting Klebsiella spp. using machine learning approaches. The project includes models, datasets, and methods to model and predict depolymerase-host interactions based on both prophage and lytic phage data.
Table of Contents

    Project Overview
    Repository Structure
    Installation
    Usage
        Data Preparation
        Model Training
        Benchmarking
    Results
    Citing DpoTropiSearch

Project Overview

Klebsiella phages use depolymerases to break down bacterial polysaccharide capsules as part of the infection process. This project leverages Klebsiella prophages and their associated depolymerase domains to predict capsular (KL) type specificity using two main machine learning approaches:

    TropiGAT - A graph attention network-based model that aggregates depolymerase embeddings to predict KL-type association.
    TropiSEQ - A sequence clustering-based model using random forests to classify KL types based on depolymerase domain presence.

These models provide an ensemble approach for predicting KL-type specificity and can generalize across prophages and lytic phages, enhancing their utility for both therapeutic and industrial applications.
Repository Structure

    data/: Jupyter notebooks for data processing and preparation, including genome downloading, prophage detection, and depolymerase domain delineation.
    model/: Scripts and resources for the TropiGAT and TropiSEQ models.
    benchmark/: Scripts for benchmarking the TropiGAT and TropiSEQ models, including metrics calculation and results compilation.
    logger/ and utils/: Logging and utility functions for data handling and model processing.
    saved/: Placeholder for model checkpoints or saved artifacts.

Installation
Requirements

    Python 3.9 or later
    Install dependencies:

    pip install -r requirements.txt

Setup

After installing dependencies, ensure the following:

    Necessary datasets are prepared using the notebooks in data/.
    Models are configured according to the model/ directory structure.

Usage
Data Preparation

Data preparation includes processing bacterial genomes, annotating depolymerase domains, and constructing the training datasets:

    Run the notebooks in data/ to download, preprocess, and annotate data for the models.

Model Training

Training the TropiGAT and TropiSEQ models requires running the appropriate scripts under model/:

    TropiGAT: Train the graph attention model for KL type prediction.
    TropiSEQ: Train the sequence clustering model for KL type prediction.

Benchmarking

The benchmarking scripts in benchmark/ allow you to evaluate model performance:

    A1.TropiGAT_benchmark.ipynb: Runs benchmarks for TropiGAT.
    A2.TropiSEQ_benchmark.ipynb: Runs benchmarks for TropiSEQ.
    B.Compile_results.ipynb: Compiles and summarizes benchmark results.

Results

Results from the TropiGAT and TropiSEQ models demonstrated effective prediction of KL type specificity in both prophages and lytic phages, particularly for KL types with substantial training data. A database of predicted depolymerase-KL associations has been generated for use in therapeutic and industrial applications.
Citing DpoTropiSearch

If you use DpoTropiSearch in your research, please cite the associated publication:

Concha-Eloko, R., Beamud, B., Domingo-Calap, P., & Sanjuán, R. (2024). Unlocking d