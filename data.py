# import pickle
# from pathlib import Path

# import pandas as pd
# import streamlit as st


# def load_file(path: str) -> pd.DataFrame:
#     with open(path, "rb") as f:
#         dataset = pickle.load(f)
#         return dataset


# @st.cache_data
# def load_data(folder: str) -> pd.DataFrame:
#     all_datasets = [load_file(file) for file in Path(folder).iterdir()]
#     df = pd.concat(all_datasets)
#     return df
import pandas as pd
from pathlib import Path

def load_data(folder):
    """
    Load data from CSV files in the specified folder.
    
    Args:
        folder (str): Path to the folder containing CSV files.
    
    Returns:
        pd.DataFrame: A DataFrame containing the concatenated data from all CSV files.
    """
    folder_path = Path(folder)
    all_datasets = []

    for file in folder_path.iterdir():
        if file.suffix == '.csv':
            dataset = pd.read_csv(file)
            all_datasets.append(dataset)

    if len(all_datasets) == 0:
        raise ValueError("No CSV files found in the specified folder.")

    # Concatenate all datasets into a single DataFrame
    df = pd.concat(all_datasets, ignore_index=True)
    return df
