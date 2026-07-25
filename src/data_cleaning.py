import pandas as pd

def load_data(df):
    print("\nFIRST FIVE RECORDS")
    print(df.head())
    
    print("\nDATASET DIMENSIONS")
    print("Rows: ", df.shape[0])
    print("Columns: ", df.shape[1])

    print("\nCOLUMN NAMES")
    print(df.columns.tolist())

    print("\nDATA TYPES AND MISSING VALUES")
    print(df.info())

    print("\nMISSING VALUES PER COLUMN")
    print(df.isnull().sum())

    print("\nDUPLICATED SUM")
    print(df.duplicated().sum())  