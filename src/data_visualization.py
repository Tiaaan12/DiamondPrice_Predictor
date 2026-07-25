import matplotlib.pyplot as plt
import seaborn as sns

def correlation_matrix(df):
    print("\nCORRELATION MATRIX")
    plt.figure(figsize=(10,8))

    sns.heatmap(df.corr(numeric_only=True),
                annot=True,
                cmap="Blues")

    plt.title("Correlation Matrix")
    plt.savefig("assets/visualization/correlation_matrix.png", dpi=300, bbox_inches='tight')
    plt.show()
    