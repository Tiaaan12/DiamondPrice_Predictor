import pandas as pd
from data_cleaning import load_data
from data_visualization import correlation_matrix
from data_visualization import price_distribution
from data_preprocessing import preprocess_data
from data_training import train_model

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
    train_model(X_train, y_train, preprocessor)



if __name__ == "__main__":
    main()