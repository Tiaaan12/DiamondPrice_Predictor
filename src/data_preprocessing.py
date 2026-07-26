from sklearn.model_selection import train_test_split
import numpy as np


def preprocess_data(df):

    X = df.drop(columns=['price'], axis=1)
    y = np.log1p(df['price'])

    print("\nFEATURES")
    print(X.head())

    print(X.columns.tolist())
    print(X.head())

    print("\nTARGET")
    print(y.head())