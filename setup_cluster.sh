
#!/bin/bash

# Configuración básica del clúster Hadoop con Spark

# Actualizar paquetes del sistema
echo "Actualizando paquetes del sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Java
echo "Instalando Java..."
sudo apt install -y openjdk-8-jdk

# Configurar variables de entorno para Java
echo "Configurando variables de entorno para Java..."
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
echo "export PATH=$PATH:$JAVA_HOME/bin" >> ~/.bashrc
source ~/.bashrc

# Descargar e instalar Hadoop
echo "Descargando e instalando Hadoop..."
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzvf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Configurar variables de entorno para Hadoop
echo "Configurando variables de entorno para Hadoop..."
echo "export HADOOP_HOME=/usr/local/hadoop" >> ~/.bashrc
echo "export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin" >> ~/.bashrc
echo "export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop" >> ~/.bashrc
source ~/.bashrc

# Descargar e instalar Spark
echo "Descargando e instalando Spark..."
wget https://downloads.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
tar -xzvf spark-3.4.1-bin-hadoop3.tgz
sudo mv spark-3.4.1-bin-hadoop3 /usr/local/spark

# Configurar variables de entorno para Spark
echo "Configurando variables de entorno para Spark..."
echo "export SPARK_HOME=/usr/local/spark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.bashrc
source ~/.bashrc

# Configurar SSH sin contraseña entre nodos
echo "Configurando SSH sin contraseña para los nodos..."
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Configurar Hadoop para un clúster pseudo-distribuido
echo "Configurando Hadoop para el modo pseudo-distribuido..."
cat <<EOL > $HADOOP_CONF_DIR/core-site.xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
EOL

cat <<EOL > $HADOOP_CONF_DIR/hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
EOL

cat <<EOL > $HADOOP_CONF_DIR/mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
EOL

cat <<EOL > $HADOOP_CONF_DIR/yarn-site.xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
EOL

echo "Formateando el sistema de archivos HDFS..."
$HADOOP_HOME/bin/hdfs namenode -format

echo "Iniciando servicios Hadoop..."
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

echo "Clúster Hadoop y Spark configurado exitosamente. ¡Listo para usar!"
