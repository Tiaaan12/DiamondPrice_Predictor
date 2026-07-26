from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

def train_model(preprocessor, X_train, y_train):
    model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

    model.fit(X_train, y_train)

    return model