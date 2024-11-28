"""
machine_learning.py
====================
Este módulo implementa modelos de regresión, clasificación y redes neuronales utilizando PySpark MLlib
y TensorFlow para entrenamiento y predicción.

Requiere:
    - PySpark MLlib
    - TensorFlow y Keras para redes neuronales
"""

from pyspark.ml.regression import LinearRegression
from pyspark.ml.classification import DecisionTreeClassifier
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

def linear_regression_model(data):
    """
    Entrena un modelo de regresión lineal en PySpark.

    Args:
        data (DataFrame): Dataset de entrada con columnas 'features' y 'label'.

    Returns:
        LinearRegressionModel: Modelo entrenado.
    """
    lr = LinearRegression(featuresCol='features', labelCol='label')
    model = lr.fit(data)
    return model

def decision_tree_classifier(data):
    """
    Entrena un clasificador de Árbol de Decisión en PySpark.

    Args:
        data (DataFrame): Dataset de entrada con columnas 'features' y 'label'.

    Returns:
        DecisionTreeClassificationModel: Modelo entrenado.
    """
    dt = DecisionTreeClassifier(featuresCol='features', labelCol='label')
    model = dt.fit(data)
    return model

def neural_network_model(input_shape):
    """
    Define y entrena una red neuronal simple usando TensorFlow/Keras.

    Args:
        input_shape (int): Tamaño de las características de entrada.

    Returns:
        Model: Modelo entrenado.
    """
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_shape,)),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
