
# Configuración de Clúster Big Data con Hadoop y Spark

Este proyecto contiene un script para configurar un clúster Big Data utilizando Hadoop y Spark en modo pseudo-distribuido.

## 🛠️ Requisitos previos
- Ubuntu 20.04 o similar
- Usuario con permisos de sudo
- Conexión a Internet

## 🚀 Pasos para la configuración

1. **Actualizar el sistema**  
   El script actualizará los paquetes instalados en tu máquina.  

2. **Instalar Java**  
   Hadoop requiere Java para funcionar. El script instala OpenJDK 8 y configura las variables de entorno necesarias.

3. **Instalar Hadoop**  
   Descarga, instala y configura Hadoop para modo pseudo-distribuido, incluyendo la configuración de HDFS, YARN y MapReduce.

4. **Instalar Spark**  
   Descarga e instala Apache Spark y configura las variables de entorno para facilitar su uso.

5. **Configurar SSH sin contraseña**  
   Se genera una clave SSH y se configura la autenticación sin contraseña para que Hadoop y Spark puedan comunicarse entre nodos.

6. **Formatear el sistema de archivos HDFS**  
   Se inicializa HDFS para almacenar datos en el clúster.

7. **Iniciar servicios**  
   Se inician los servicios de Hadoop y Spark.

## 💻 Uso del clúster
Una vez configurado, puedes usar el clúster para procesamiento de datos masivos. Ejemplo: ejecutar scripts de PySpark.

## 📝 Notas
- Este script configura un entorno de desarrollo en modo pseudo-distribuido (un solo nodo). Para un clúster real, añade más nodos y ajusta las configuraciones.
- Asegúrate de revisar los archivos de configuración en `HADOOP_HOME/etc/hadoop` para personalizar el entorno.

## 📂 Archivos en este repositorio
- `setup_cluster.sh`: Script de configuración del clúster.
- `README.md`: Este archivo.

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, no dudes en abrir un pull request.

---

**Autor:** [Tu Nombre]  
**Licencia:** MIT
