import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def show_prediction(model, X_test, y_test):
    log_predictions = model.predict(X_test)
    predictions = np.expm1(log_predictions)
    actual = np.expm1(y_test)

    return actual, predictions

def show_model_coefficients(model):
    regressor = model.named_steps["regressor"]

    print("\nMODEL INTERCEPT")
    print(f"{regressor.intercept_:.4f}")

    feature_names = model.named_steps["preprocessor"].get_feature_names_out()

    coefficient_table = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": regressor.coef_
    })

    print("\nMODEL COEFFICIENTS")
    print(coefficient_table.round(4))

    print("\nINTERPRETATION OF COEFFICIENTS")

    for feature, coefficient in zip(feature_names, regressor.coef_):

        direction = "increase" if coefficient >= 0 else "decrease"

        print(
            f"A one-unit increase in {feature}, while holding the other "
            f"features constant, is associated with a {direction} of "
            f"{abs(coefficient):.4f} in the predicted log diamond price."
        )

def show_model_residuals(model, actual, predictions, X_test, y_test):
    log_predictions = model.predict(X_test)

    actual = np.expm1(y_test)
    predictions = np.expm1(log_predictions)

    results = X_test.copy()

    results["Actual Price ($)"] = actual.values
    results["Predicted Price ($)"] = predictions

    results["Residual ($)"] = (
        results["Actual Price ($)"] -
        results["Predicted Price ($)"]
    )

    results["Absolute Error ($)"] = (
        results["Residual ($)"].abs()
    )

    print("\nACTUAL AND PREDICTED DIAMOND PRICES")
    print(results.round(2))

def evaluate_model(actual, predictions):
    mae = mean_absolute_error(actual, predictions)
    mse = mean_squared_error(actual, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predictions)

    print("\nMODEL EVALUATION")
    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²  : {r2:.4f}")

    print("\nEVALUATION INTERPRETATION")
    print(
        f"On average, the model's predictions differ from the actual"
        f"diamond prices by approximately {mae:.2f}, based on MAE."
    )

    if r2 >= 0.90:
        print("The model explains the variation in the data very well")
    elif r2 >= 0.70:
        print("The model demonstrates reasonably good predictive performance")
    elif r2 >= 0.50:
        print("The model demonstrates moderate predictive performance.")
    else:
        print("The model has limited predictive performance and may require "
        "more data or additional relevant features.")
