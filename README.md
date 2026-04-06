# Project Data Science 
Este repositorio contiene el desarrollo completo de un proyecto de análisis de datos enfocado en depresión estudiantil, incluyendo procesamiento, análisis exploratorio, visualización y generación de reportes.

## 📁 Estructura del Proyecto
```bash
Project-data-science-1-main/
│
├── data/
│   ├── processed/ # Datos limpios y transformados
│   │   └── Student_Depression_Dataset_codificado.csv
│   │   └── Student_Depression_Dataset_Limpio.csv
│   │
│   └── raw/ # Datos originales sin procesar
│       └── Student_Depression_Dataset_Original.csv
│
├── docs/ # Documentación del proyecto
│   └── Informe SCY1101.pdf
│
├── notebooks/ # Jupyter notebooks del análisis
│   ├── Fase_1_2A_setup_y_EDA.ipynb
│   ├── Fase_2B_limpieza.ipynb
│   └── Fase_3_Codificacion_documentada.ipnyb
│   └── Fase_4_análisis_datos.ipynb
│
├── outputs/
│   └── figures/ # Visualizaciones generadas
│       ├── 01_distribucion_etaria_depresion.png
│       ├── 02_presion_academica_carreras.png
│       ├── 03_influencia_variables_en_depresion.png
│       ├── 04_satisfaccion_estudios_segun_cgpa.png
│       ├── 05_comparacion_sueño_alimentacion.png
│       └── 06_heatmap_correlacion.png
│
├── reports/ # Resultados y reportes en CSV
│   ├── 00_resumen_estadistico_general.csv
│   ├── 01_distribucion_general_depresion.csv
│   ├── 02_proporcion_pensamientos_por_genero.csv
│   ├── 03_proporcion_depresion_por_genero.csv
│   ├── 04_influencia_sueño_en_depresion.csv
│   ├── 05_top_10_ciudades_mayor_depresion.csv
│   └── 06_cgpa_y_presion_segun_horas_estudio.csv
│
├── src/ # Código fuente reutilizable
│   ├── carga.py
│   ├── eda_utils.py
└── environment.yml
│
└── README.md
```

## Tecnologías utilizadas
* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* Jupyter Notebook
* SciPy
* Scikit-learn
* Conda

## Flujo del proyecto
1. Carga de datos &rarr; `src/carga.py`
2. Limpieza &rarr; `notebooks/Fase_2B_limpieza.ipynb`
3. EDA (Exploratory Data Analysis) &rarr; `notebooks/Fase_1_2A_setup_y_EDA.ipynb`
4. Codificación de variables &rarr; `notebooks/Fase_3_Codificación.ipynb`
5. Análisis final &rarr; `notebooks/Fase_4_análisis_datos.ipynb`
6. Visualizaciones &rarr; `outputs/figures/`
7. Reportes finales &rarr; `outputs/reports/`

## Objetivo
Analizar factores que influyen en la depresión en estudiantes, considerando variables como:
* Presión académica
* Horas de sueño
* Alimentación
* Género
* Rendimiento académico (CGPA)

## Documentación
El informe completo del proyecto se encuentra en:
```bash
docs/Informe SCY1101.pdf
```

## Cómo usar el proyecto
1. Clonar el repositorio:
```bash
git clone https://github.com/0Trickster/Project-data-science-1
cd Project-data-science-1-main
```
2. Crear entorno
```bash
conda env create -f environment.yml
conda activate <env-name>
```
3. Ejecutar notebooks:
```bash
jupyter notebook
```