# DpoTropiSearch

This repository contains the implementation and data for **DpoTropiSearch**, a research project aimed at predicting the capsular type-specificity of phage depolymerases targeting *Klebsiella* spp. using machine learning approaches. The project includes models, datasets, and methods to model and predict depolymerase-host interactions based on both prophage and lytic phage data.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Preparation](#data-preparation)
  - [Model Training](#model-training)
  - [Benchmarking](#benchmarking)
- [Results](#results)
- [Citing DpoTropiSearch](#citing-dpotropisearch)

## Project Overview

*Klebsiella* spp. often express polysaccharide capsules that act as barriers to phage infection. Many *Klebsiella* phages encode depolymerases to degrade these capsules, driving a co-evolutionary arms race. This project leverages prophage-encoded depolymerases and machine learning models to predict capsular tropism. By integrating sequence clustering and directed acyclic graph approaches, the study demonstrates the predictability of phage-host interactions at the subspecies level, offering valuable insights for phage therapy and industrial applications.

## Repository Structure

The repository is organized as follows:

- `benchmark/` - Contains benchmarking scripts and results.
- `data_collection/` - Scripts and data related to the collection and preprocessing of datasets.
- `scripts/` - Contains notebooks to allow the use of the models on your own data.
- `trainer/` - Includes model training scripts, optimization, and evaluations.
- `utils/` - Utility scripts and helper functions.
- `other/` - Miscellaneous files and scripts.
- `README.md` - This README file.

## Installation

To set up the project environment, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/conchaeloko/DpoTropiSearch.git
   cd DpoTropiSearch
   ```

2. **Install dependencies:**

   To use the methods developed in the study, install and activate the Conda environment using the corresponding YAML file:

   - **TropiGAT** -> `TropiGAT_env.yml`
   - **TropiSEQ** -> `TropiSEQ_env.yml`

   Ensure you have a recent version of Conda installed. Then, create the Conda environment using the following command:

   ```bash
   conda env create -f environment.yml
   ```

## Usage

### Data Preparation

Before training the models, ensure that the datasets are properly prepared:

1. **Data Collection:**

   Use the scripts in the `data_collection/` directory to gather and preprocess the necessary data.

2. **Data Formatting:**

   Ensure that the data is formatted correctly for model training. Refer to the scripts and documentation in the `data_collection/` directory for guidance.

### Model Training

To train the model:

1. **Configure Training Parameters:**

   Modify the configuration files in the `trainer/` directory to set your desired training parameters.

2. **Start Training:**

   Explore the training notebook corresponding to the method you want to train.

   *Example: Use `A1.training_TropiGAT.ipynb` to train the model using your data.*

### Benchmarking

To evaluate the model's performance:

1. **Run Benchmarking Scripts:**

   Use the scripts in the `benchmark/` directory to assess the model's performance.

## Results

The results of the model training and benchmarking, including performance metrics and visualizations, can be found in the `benchmark/` and `other/` directories. Detailed analyses and discussions are provided within the respective files.

## Citing DpoTropiSearch

If you use this code or data in your research, please cite the associated publication:

```
Concha Eloko, Robby, Rafael Sanjuan, Beatriz Beamud, and Pilar Domingo-Calap. "Unlocking data in Klebsiella lysogens to predict capsular type-specificity of phage depolymerases." bioRxiv (2024): 2024-07.
```

---

For any questions or issues, please open an issue in this repository or contact the authors directly.
