import pandas as pd

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output_cleaned.csv"

def clean_data():
    df = pd.read_csv(INPUT_FILE)

    # Remove empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Trim spaces in column names
    df.columns = df.columns.str.strip()

    # Trim spaces in string values
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    df.to_csv(OUTPUT_FILE, index=False)
    print("Data cleaned successfully.")

if __name__ == "__main__":
    clean_data()
