# Explainable-Drug-discovery

## Project Architecture

```mermaid
flowchart TD

A[Drug Molecule SMILES]
--> B[Molecular Graph]

B --> C[Graph Neural Network]

C --> D[Drug Embedding]

C --> E[GNNExplainer / PGExplainer]

F[Patient Omics Data]
--> G[Gene Expression Encoder]

G --> H[Omics Embedding]

D --> I[Multimodal Fusion]
H --> I

I --> J[Drug Response Prediction]

J --> K[IC50 Prediction]
J --> L[Sensitivity Prediction]

K --> M[Translational Medicine]
L --> M

M --> N[Pathway Analysis]
M --> O[Biomarker Discovery]
```
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
