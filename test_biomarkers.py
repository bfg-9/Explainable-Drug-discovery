from src.biomarkers import load_biomarkers


genes, names = load_biomarkers()


print(
    genes.shape
)


print(
    names
)