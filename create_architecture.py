import matplotlib.pyplot as plt


fig, ax = plt.subplots(
    figsize=(12,8)
)


ax.axis(
    "off"
)


def box(
    text,
    x,
    y
):

    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=11,
        bbox=dict(
            boxstyle="round,pad=0.5"
        )
    )


def arrow(
    x1,
    y1,
    x2,
    y2
):

    ax.annotate(
        "",
        xy=(x2,y2),
        xytext=(x1,y1),
        arrowprops=dict(
            arrowstyle="->",
            lw=2
        )
    )


# Drug branch

box(
    "Drug SMILES",
    0.25,
    0.9
)

box(
    "Molecular Graph\n(Atoms + Bonds)",
    0.25,
    0.75
)

box(
    "Graph Attention Network\n(GAT Encoder)",
    0.25,
    0.55
)


arrow(
    0.25,0.86,
    0.25,0.79
)

arrow(
    0.25,0.70,
    0.25,0.60
)


# Gene branch

box(
    "DepMap Gene Expression",
    0.75,
    0.9
)


box(
    "Biomarker Encoder\nTP53 EGFR KRAS\nBRAF MYC",
    0.75,
    0.65
)


arrow(
    0.75,0.85,
    0.75,0.72
)


# Fusion

box(
    "Multimodal Fusion Layer",
    0.5,
    0.40
)


arrow(
    0.28,0.52,
    0.45,0.43
)

arrow(
    0.72,0.60,
    0.55,0.43
)


box(
    "Drug Response Prediction",
    0.5,
    0.25
)


arrow(
    0.5,0.36,
    0.5,0.29
)


# Explainability

box(
    "GNNExplainer\nAtom Importance",
    0.25,
    0.10
)


box(
    "SHAP\nBiomarker Importance",
    0.75,
    0.10
)


arrow(
    0.43,0.24,
    0.28,0.14
)

arrow(
    0.57,0.24,
    0.72,0.14
)


plt.title(
    "Explainable Multimodal GAT Framework for Cancer Drug Response Prediction",
    fontsize=14
)


plt.savefig(
    "figures/Figure1_architecture.png",
    dpi=300,
    bbox_inches="tight"
)


plt.close()


print(
    "Generated figures/Figure1_architecture.png"
)