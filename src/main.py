import pandas as pd
from data_cleaning import load_data
from data_visualization import correlation_matrix
from data_visualization import price_distribution
from data_preprocessing import preprocess_data
from data_training import train_model
from model_evaluation import show_prediction, show_model_coefficients, show_model_residuals, evaluate_model

file_path = "data/raw/diamonds.csv"

def main():
    try:
        df = pd.read_csv(file_path)
        print("Dataset load successfully.")
    except:
        raise FileNotFoundError(
            f"Dataset not found at: (file_path)\n"
            "Upload the CSV file and update the file_path variable"
        )

    load_data(df)
    correlation_matrix(df)
    price_distribution(df)
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)
    model = train_model(X_train, y_train, preprocessor)
    actual, predictions = show_prediction(model, X_test, y_test)
    show_model_coefficients(model)
    show_model_residuals(model, actual, predictions, X_test, y_test)
    evaluate_model(actual, predictions)




if __name__ == "__main__":
    main()