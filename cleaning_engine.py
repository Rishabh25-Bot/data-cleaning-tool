import pandas as pd

def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    return df, before - after

def remove_high_missing_columns(df, threshold=40):
    missing_percent = df.isnull().mean() * 100
    cols_to_drop = missing_percent[missing_percent > threshold].index
    df = df.drop(columns=cols_to_drop)
    return df, list(cols_to_drop)

def fill_missing_values(df):
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df
