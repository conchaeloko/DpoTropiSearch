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

*Klebsiella* phages use depolymerases to break down bacterial polysaccharide capsules as part of the infection process. Understanding and predicting the specificity of these depolymerases can aid in developing phage therapies and understanding phage-host interactions. This project leverages machine learning techniques to predict the capsular type-specificity of phage depolymerases.

## Repository Structure

The repository is organized as follows:

- `benchmark/` - Contains benchmarking scripts and results.
- `data_collection/` - Scripts and data related to the collection and preprocessing of datasets.
- `trainer/` - Includes model training scripts and configurations.
- `utils/` - Utility scripts and helper functions.
- `other/` - Miscellaneous files and scripts.
- `LICENSE` - License information for the project.
- `README.md` - This README file.

## Installation

To set up the project environment, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/conchaeloko/DpoTropiSearch.git
   cd DpoTropiSearch
   ```

2. **Install dependencies:**

   Ensure you have [Python 3.x](https://www.python.org/downloads/) installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: The `requirements.txt` file should list all necessary dependencies.*

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

   Run the training script:

   ```bash
   python trainer/train.py
   ```

   *Note: Replace `train.py` with the actual training script filename if it differs.*

### Benchmarking

To evaluate the model's performance:

1. **Run Benchmarking Scripts:**

   Use the scripts in the `benchmark/` directory to assess the model's accuracy and other performance metrics.

## Results

The results of the model training and benchmarking, including performance metrics and visualizations, can be found in the `benchmark/` directory. Detailed analyses and discussions are provided within the respective files.

## Citing DpoTropiSearch

If you use this code or data in your research, please cite the associated publication:

```
[Authors]. "Unlocking data in Klebsiella lysogens to predict capsular type-specificity of phage depolymerases." bioRxiv (2024). DOI: 10.1101/2024.07.24.604748
```

*Note: Replace `[Authors]` with the actual author names as listed in the publication.*

---

For any questions or issues, please open an issue in this repository or contact the authors directly.
