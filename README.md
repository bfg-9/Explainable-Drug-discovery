# Explainable-Drug-discovery

## Project Architecture
Drug Molecule (SMILES)
          │
          ▼
 Molecular Graph
          │
          ▼
     Graph GNN
          │
          ├────────────┐
          │            │
          ▼            ▼
 Drug Embedding    Explanation Module
          │        (GNNExplainer/PGExplainer)
          │
          ▼
Patient Omics Data
(Gene Expression)
          │
          ▼
 Multimodal Fusion
          │
          ▼
 Drug Response Prediction
(IC50 / Sensitivity)
          │
          ▼
 Translational Medicine Layer
(Pathway Analysis + Biomarkers)

## Project Structure
ExplainableDrugDiscovery/

│
├── data/
│   ├── drugs.csv
│   ├── gene_expression.csv
│   └── response.csv
│
├── models/
│   ├── gnn.py
│   ├── fusion.py
│   └── predictor.py
│
├── explainability/
│   ├── gnn_explainer.py
│   └── shap_analysis.py
│
├── training/
│   └── train.py
│
├── utils/
│   └── data_loader.py
│
└── requirements.txt
