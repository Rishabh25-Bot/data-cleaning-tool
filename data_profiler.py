import pandas as pd

def profile_data(df):
    profile = {}

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]

    profile["dtypes"] = df.dtypes.astype(str)

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    profile["missing"] = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing %": missing_percent.round(2)
    })

    profile["duplicates"] = df.duplicated().sum()

    profile["summary"] = df.describe(include="all")

    return profile
