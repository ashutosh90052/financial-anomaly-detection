import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    df = df.dropna()
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.dayofweek
    return df
