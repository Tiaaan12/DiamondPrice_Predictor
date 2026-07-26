import numpy as np
import pandas as pd

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