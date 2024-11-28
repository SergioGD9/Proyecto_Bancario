"""
data_processing.py
==================
Este módulo utiliza PySpark para el procesamiento de datos estructurados y no estructurados,
realizando transformaciones y generando datasets limpios para modelado de Machine Learning.

Requiere:
    - PySpark instalado
    - Conexión a HDFS para cargar los datos

"""

from pyspark.sql import SparkSession

def start_spark_session(app_name: str):
    """
    Inicia una sesión de Spark.

    Args:
        app_name (str): Nombre de la aplicación de Spark.

    Returns:
        SparkSession: Objeto de sesión Spark.
    """
    return SparkSession.builder.appName(app_name).getOrCreate()

def clean_structured_data(spark: SparkSession, file_path: str):
    """
    Limpia y transforma datos estructurados desde un archivo en HDFS.

    Args:
        spark (SparkSession): Sesión de Spark.
        file_path (str): Ruta del archivo en HDFS.

    Returns:
        DataFrame: DataFrame limpio listo para análisis.
    """
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    df_cleaned = df.na.drop()
    return df_cleaned

def process_unstructured_text(spark: SparkSession, text_path: str):
    """
    Procesa texto no estructurado usando técnicas de NLP.

    Args:
        spark (SparkSession): Sesión de Spark.
        text_path (str): Ruta del archivo de texto.

    Returns:
        DataFrame: DataFrame con tokens limpios.
    """
    from pyspark.ml.feature import Tokenizer
    text_df = spark.read.text(text_path)
    tokenizer = Tokenizer(inputCol="value", outputCol="words")
    tokenized_df = tokenizer.transform(text_df)
    return tokenized_df
