# Explainable Multimodal Graph Neural Network for Cancer Drug Response Prediction

## Overview

Drug response prediction is a critical challenge in precision oncology. 
Traditional machine learning models can predict sensitivity patterns but often lack biological and molecular interpretability.

This project develops an Explainable AI framework that integrates:

- Molecular structure information from drug compounds
- Cancer cell-line gene expression profiles
- Graph Neural Networks
- Explainability techniques

The objective is not only to predict drug response but also identify the molecular substructures and genomic biomarkers contributing to model decisions.


---

# Research Question

Can an explainable multimodal deep learning model combine molecular structure and cancer genomic information to improve interpretation of cancer drug response prediction?


---

# Framework Architecture


![Architecture](figures/Figure1_architecture.png)


The framework consists of two learning branches:

## Molecular Encoder

Drug SMILES representations are converted into molecular graphs:

- Nodes: atoms
- Edges: chemical bonds

A Graph Attention Network learns molecular representations.


## Biological Encoder

Cancer cell-line gene expression data is processed using selected oncogenic biomarkers:

- TP53
- EGFR
- KRAS
- BRAF
- MYC
- PIK3CA
- PTEN
- BRCA1
- BRCA2
- ALK
- ERBB2


The molecular and biological embeddings are combined using a fusion network.


---

# Datasets

## PRISM Drug Response Dataset

Used for:

- Drug sensitivity measurements
- Dose-response information
- Compound screening data


## DepMap Gene Expression Dataset

Used:

OmicsExpressionProteinCodingGenesTPMLogp1

Contains:

- 1600+ cancer cell lines
- 19000+ gene expression features


---

# Methodology


## Molecular Representation

- RDKit molecular processing
- Atom feature extraction
- Molecular graph construction


## Deep Learning Models

Implemented:

- Graph Convolutional Network
- Graph Attention Network
- Multimodal Fusion Network


## Baseline Models

Compared against:

- Random Forest
- XGBoost
- Multi Layer Perceptron


---

# Explainable AI


## Molecular Explainability

GNNExplainer identifies important atoms and molecular regions influencing prediction.


![Atom Explanation](figures/Figure2_GNN_atom_explanation.png)


---

## Biological Explainability

SHAP analysis identifies influential cancer biomarkers.


![SHAP Biomarkers](figures/Figure3_SHAP_biomarkers.png)


---

# Results


## Prediction Performance


![Prediction](figures/Figure4_prediction_performance.png)


## Model Comparison


| Model | Input Features | R2 Score |
|---|---|---|
| Random Forest | Morgan Fingerprint + Genes | 0.804 |
| XGBoost | Morgan Fingerprint + Genes | 0.805 |
| MLP | Morgan Fingerprint + Genes | 0.759 |
| GNN | Molecular Graph | 0.659 |
| GAT Fusion | Molecular Graph + Genes | Experimental Model |


---

# Key Findings


- Molecular representations significantly improve drug response prediction.
- Cancer biomarkers provide biological context for model decisions.
- Traditional fingerprints remain highly competitive.
- Graph-based approaches provide molecular-level interpretability.
- Combining GNNExplainer and SHAP enables dual explainability.


---

# Technologies Used

- Python
- PyTorch
- PyTorch Geometric
- RDKit
- SHAP
- Scikit-learn
- XGBoost
- DepMap
- PRISM


---

# Future Improvements

- Integration of whole transcriptomic profiles
- Pathway-level biological modelling
- Transformer-based molecular encoders
- Multi-omics fusion
- Clinical validation


---

# Research Direction

This project explores interpretable AI systems for precision oncology by combining computational drug discovery, graph representation learning, and explainable artificial intelligence.