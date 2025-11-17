import pandas as pd
from pandas import DataFrame as DataFrame


def load(path: str) -> DataFrame | None:

    try:
        df = pd.read_csv(path)
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print("Error: unable to load image")
        return None

    print("Loading DataFrame of dimension : " + "(", df.shape[0], ",", df.shape[1], ")")
    return df
