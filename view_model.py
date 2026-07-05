import torch


model_file = "drug_response_gnn.pt"


checkpoint = torch.load(
    model_file,
    map_location=torch.device("cpu")
)


print("\nMODEL CONTENT:\n")


for layer, weights in checkpoint.items():

    print("--------------------------------")
    
    print("Layer Name:", layer)

    print("Shape:", weights.shape)

    print("Values:")

    print(weights[:5])