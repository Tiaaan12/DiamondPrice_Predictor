import matplotlib.pyplot as plt
import seaborn as sns

def correlation_matrix(df):
    plt.figure(figsize=(10,8))

    sns.heatmap(df.corr(numeric_only=True),
                annot=True,
                cmap="Blues")

    plt.title("Correlation Matrix")
    plt.savefig("assets/visualization/correlation_matrix.png", dpi=300, bbox_inches='tight')
    plt.show()

def price_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['price'], bins=50)
    plt.title("Price Distribution")
    plt.savefig("assets/visualization/price_distribution.png", dpi=300, bbox_inches='tight')
    plt.show()
    