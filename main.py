
from src.biomarkers import load_biomarkers


import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch

from src.preprocess import load_data
from src.molecular_graph import smiles_to_graph
from src.train_gcn_backup import DrugResponseGNN


from torch_geometric.loader import DataLoader

gene_tensor, gene_names = load_biomarkers()


print(
    "Gene data loaded:",
    gene_tensor.shape
)

dataset = []


df = load_data()

for _, row in df.iterrows():

    try:

        graph = smiles_to_graph(
            row["smiles"]
        )


        if graph is None:
            continue


        graph.y = torch.tensor(
            [row["auc"]],
            dtype=torch.float
        )


        index = len(dataset) % gene_tensor.shape[0]


        graph.genes = gene_tensor[
            index
        ]


        dataset.append(graph)


    except Exception as e:

        continue

        dataset.append(graph)


    except Exception as e:

        continue



loader=DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)



model=DrugResponseGNN()



optimizer=torch.optim.Adam(
    model.parameters(),
    lr=0.001
)



loss_fn=torch.nn.MSELoss()



for epoch in range(50):

    total_loss = 0


    for batch in loader:


        optimizer.zero_grad()


        genes = batch.genes.view(
            batch.num_graphs,
            -1
        )


        pred = model(
            batch.x,
            batch.edge_index,
            batch.batch,
            genes
        )


        loss = loss_fn(
            pred,
            batch.y.view(-1,1)
        )


        loss.backward()


        optimizer.step()


        total_loss += loss.item()


    print(
        epoch,
        total_loss
    )


torch.save(
    model.state_dict(),
    "gat_fusion_drug_response.pt"
)


print(
    "MODEL SAVED SUCCESSFULLY"
)


print("MODEL SAVED SUCCESSFULLY")


from src.explain import explain_model


print("STARTING GNN EXPLAINER")


sample_graph = dataset[0]


explanation = explain_model(
    model,
    sample_graph
)


print("EXPLANATION FINISHED")

from src.evaluate import evaluate_model


evaluate_model(
    model,
    loader
)

from src.shap_explain import explain_biomarkers


explain_biomarkers(

    model,

    loader,

    gene_names

)
from src.baseline_models import run_baselines


import numpy as np


from src.baseline_models import run_baselines

from src.fingerprints import smiles_to_fingerprint


import numpy as np



from src.baseline_models import run_baselines

from src.fingerprints import smiles_to_fingerprint

import numpy as np


# create fresh Python lists

baseline_X_list = []

baseline_y_list = []


for _, row in df.iterrows():

    fp = smiles_to_fingerprint(
        row["smiles"]
    )


    if fp is None:
        continue


    gene_index = (
        len(baseline_X_list)
        %
        gene_tensor.shape[0]
    )


    genes = gene_tensor[
        gene_index
    ].numpy()


    combined_features = np.concatenate(
        [
            fp,
            genes
        ]
    )


    baseline_X_list.append(
        combined_features
    )


    baseline_y_list.append(
        row["auc"]
    )


# convert only AFTER loop finishes

baseline_X = np.array(
    baseline_X_list
)


baseline_y = np.array(
    baseline_y_list
)


print(
    "Baseline feature matrix:",
    baseline_X.shape
)


run_baselines(
    baseline_X,
    baseline_y
)