def cargar_csv(ruta):
    import pandas as pd
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print("Archivo no encontrado")