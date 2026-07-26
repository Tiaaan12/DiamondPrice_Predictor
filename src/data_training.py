from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import joblib

def train_model(preprocessor, X_train, y_train):
    model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

    model.fit(X_train, y_train)

    joblib.dump(model, 'model/linear_regress_diamond.pkl')

    return model