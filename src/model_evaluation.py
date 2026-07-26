import numpy as np

def show_prediction(model, X_test, y_test):
    log_predictions = model.predict(X_test)
    predictions = np.expm1(log_predictions)
    actual = np.expm1(y_test)

    return actual, predictions