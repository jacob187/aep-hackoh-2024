import pandas as pd
import os


# Read the CSV file from the files directory
def read_aep_csv() -> pd.DataFrame:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "../../../files/data1.csv")

    # Read the CSV file
    return pd.read_csv(csv_path)


def read_pk(file_path: str) -> pd.DataFrame:
    return pd.read_pickle(file_path)


def save_pk(df: pd.DataFrame, file_path: str):
    df.to_pickle(file_path)


if __name__ == "__main__":
    df = read_aep_csv()
