import pandas as pd

def eliminar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina valores nulos"""
    valores_n=df.isnull().sum()
    print(f"Tiene: {valores_n} nulos")
    return df.dropna()