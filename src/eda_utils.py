# Funciones de detección de outliers y duplicados 

def detectar_outliers_iqr(df):

    resultados = {}
    columnas_numericas = df.select_dtypes(include='number').columns

    for col in columnas_numericas:
        serie = df[col].dropna()
        Q1 = serie.quantile(0.25)
        Q3 = serie.quantile(0.75)
        IQR = Q3 - Q1

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        mascara = (serie < limite_inferior) | (serie > limite_superior)

        resultados[col] = {
            "skew": serie.skew(),
            "cantidad_outliers": mascara.sum(),
            "limite_inferior": limite_inferior,
            "limite_superior": limite_superior
        }

    return resultados


def detectar_outliers_3sigmas(df):

    resultados = {}
    columnas_numericas = df.select_dtypes(include='number').columns

    for col in columnas_numericas:
        serie = df[col].dropna()

        media = serie.mean()
        std = serie.std()

        limite_inferior = media - 3 * std
        limite_superior = media + 3 * std

        mascara = (serie < limite_inferior) | (serie > limite_superior)

        resultados[col] = {
            "skew": serie.skew(),
            "cantidad_outliers": mascara.sum(),
            "limite_inferior": limite_inferior,
            "limite_superior": limite_superior
        }

    return resultados


def eliminar_outliers_3sigmas(serie):
    media = serie.mean()
    std = serie.std()

    limite_inferior = media - 3 * std
    limite_superior = media + 3 * std

    mascara = (serie < limite_inferior) | (serie > limite_superior)

    return mascara, limite_inferior, limite_superior


# DEPRECADO: no se hallaron duplicados que deban borrarse
def detectar_duplicados(df):

    resultados = {}

    for col in df.columns:

        duplicados = df[col].duplicated().sum()

        resultados[col] = {
            "cantidad_duplicados": duplicados
        }

    return resultados