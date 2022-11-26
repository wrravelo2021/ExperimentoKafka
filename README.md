# Experimento Kafka

## Pre-requisitos

- Python 3.10.6
- Kafka

## Correr Kafka



## Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r ./requirements.txt
```

## Ejecutar broker Zookeeper

```bash
/opt/homebrew/opt/kafka/bin/zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```

## Ejecutar Kafka

```bash
/opt/homebrew/opt/kafka/bin/kafka-server-start /opt/homebrew/etc/kafka/server.properties
```

## Crear topic

```bash
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic miso
```

## Ejecutar subscriptor

```bash
python subscriber.py
```

## Ejecutar publicador

```bash
python publisher.py
```

## Ejecutar servidor

```bash
FLASK_ENV=development FLASK_APP=server.py python -m flask run
```