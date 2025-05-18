import pandas as pd

def describe_data(df):
    description = df.describe(include='all').transpose()
    nulls = df.isnull().sum()
    types = df.dtypes

    summary = pd.DataFrame({
        "Data Type": types,
        "Missing Values": nulls,
    })

    return summary.join(description)
