import pandas as pd

def load_csv(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = [col.strip() for col in df.columns]  # Clean column names
        return df
    except Exception as e:
        raise ValueError(f"Error reading CSV: {e}")
