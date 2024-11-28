"""
data_ingestion.py
=================
Este módulo contiene funciones para la ingesta de datos estructurados y no estructurados
en un sistema Hadoop Distributed File System (HDFS) y la configuración de un pipeline
en tiempo real utilizando Apache Kafka.

Requiere:
    - Hadoop y HDFS configurados en el sistema
    - Apache Kafka para ingesta en tiempo real
"""

from kafka import KafkaProducer
import os
from hdfs import InsecureClient

def upload_to_hdfs(local_path: str, hdfs_path: str, hdfs_client_url: str):
    """
    Sube un archivo local al sistema HDFS.

    Args:
        local_path (str): Ruta del archivo local.
        hdfs_path (str): Ruta de destino en HDFS.
        hdfs_client_url (str): URL del cliente HDFS (e.g., "http://localhost:50070").

    Returns:
        None
    """
    client = InsecureClient(hdfs_client_url)
    with open(local_path, 'rb') as file_data:
        client.write(hdfs_path, file_data)
    print(f"Archivo {local_path} subido exitosamente a {hdfs_path} en HDFS.")

def stream_to_kafka(topic: str, message: str, kafka_server: str):
    """
    Envía un mensaje a un tema de Kafka.

    Args:
        topic (str): Tema de Kafka donde se enviará el mensaje.
        message (str): Mensaje a enviar.
        kafka_server (str): Dirección del servidor Kafka (e.g., "localhost:9092").

    Returns:
        None
    """
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()
    print(f"Mensaje enviado al tema {topic} en Kafka.")
