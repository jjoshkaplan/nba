"""load csv data for advanced NBA statistics across any year for regular season or playoffs"""

import pandas as pd


def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Load data from csv file
    :param file_path: Path to CSV File
    :return: Dataframe
    """
    df = pd.read_csv(file_path)
    return df
