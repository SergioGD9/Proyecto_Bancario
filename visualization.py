"""
visualization.py
=================
Este módulo utiliza Matplotlib y Seaborn para visualizar resultados de los modelos.

Requiere:
    - Matplotlib
    - Seaborn
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_results(results, title):
    """
    Grafica los resultados de predicciones.

    Args:
        results (dict): Diccionario con datos a graficar.
        title (str): Título del gráfico.

    Returns:
        None
    """
    sns.barplot(x=list(results.keys()), y=list(results.values()))
    plt.title(title)
    plt.ylabel('Score')
    plt.show()
