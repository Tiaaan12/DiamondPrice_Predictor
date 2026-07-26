from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):

    X = df.drop(columns=['price'], axis=1)
    y = np.log1p(df['price'])

    print("\nFEATURES")
    print(X.head())

    print(X.columns.tolist())
    print(X.head())

    print("\nTARGET")
    print(y.head())

    categorical_features = ["cut", "color", "clarity"]

    numerical_features = [
        "carat",
        "depth",
        "table",
        "x",
        "y",
        "z"
    ]
    preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(drop="first"),
            categorical_features
        )
    ]
)