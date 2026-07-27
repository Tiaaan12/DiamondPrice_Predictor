import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

def predictions_scatter_plot(model, X_test, y_test):
    predictions = np.expm1(model.predict(X_test))

    actual = np.expm1(y_test)

    plt.figure(figsize=(8,6))

    plt.scatter(
        actual,
        predictions,
        s=70,
        alpha=0.6
    )

    minimum_price = min(actual.min(), predictions.min())
    maximum_price = max(actual.max(), predictions.max())

    plt.plot(
        [minimum_price, maximum_price],
        [minimum_price, maximum_price],
        linestyle="--",
        color="red",
        linewidth=2
    )

    plt.xlabel("Actual Diamond Price ($)")
    plt.ylabel("Predicted Diamond Price ($)")
    plt.title("Actual versus Predicted Diamond Prices")

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("assets/visualization/prediction_scatter_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

def residuals_scatter_plot(actual, predictions):
    residuals = actual - predictions
    

    plt.figure(figsize=(8, 6))
    plt.scatter(
        predictions,
        residuals,
        s=70,
        alpha=0.6
    )

    plt.axhline(
        y=0,
        color="red",
        linestyle="--"
    )
    plt.xlabel("Predicted Diamond Price ($)")
    plt.ylabel("Residual (Acutal - Predicted)")
    plt.title("Residual Plot for Diamond Price Prediction")
    plt.grid(alpha=0.3),
    plt.tight_layout()
    plt.savefig("assets/visualization/residual_scatter_plot.png", dpi=300, bbox_inches='tight')
    plt.show()
    
    