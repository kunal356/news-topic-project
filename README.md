# Real-Time News Streaming with Confluent Kafka, Azure Databricks, and CosmosDB

This repository demonstrates a real-time news streaming application leveraging **Confluent Kafka**, **Azure Databricks**, and **CosmosDB** for a robust and scalable solution to fetch, process, and store live news data.

## Overview
- **Confluent Kafka**: Streams live news data in real-time.
- **Azure Databricks**: Utilizes Spark Structured Streaming for efficient data processing and analysis.
- **CosmosDB (MongoDB API)**: Stores processed news data for retrieval and further analytics.

## Key Components
1. **Kafka Producers and Consumers**: 
   - Producers stream live news data into Kafka topics.
   - Consumers process streamed data for analytics or storage.

2. **Azure Databricks with Spark**:
   - Spark Structured Streaming processes Kafka data in real-time.
   - Databricks notebooks (`spark-stream.ipynb`) manage the streaming and data transformation pipelines.

3. **CosmosDB (MongoDB API)**:
   - Stores transformed news data in a scalable and globally distributed NoSQL database.
   - Enables real-time querying and analytics on processed news topics.

## Prerequisites
- [Confluent Kafka](https://www.confluent.io/)
- [Azure Databricks](https://azure.microsoft.com/en-us/products/databricks/)
- [Azure CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db/)
- [Python 3.8+](https://www.python.org/)
- Required Python libraries (`requirements.txt`).

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/kunal356/news-topic-project.git
cd news-topic-project
```

### 2. Set Up Kafka
1. Install and configure Confluent Kafka.
2. Start Kafka services and create the necessary topics:
   ```bash
   kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic news-stream
   ```

### 3. Set Up Azure Databricks
1. Configure Databricks cluster and upload the `spark-stream.ipynb` notebook.
2. Connect Databricks to Kafka for data ingestion and CosmosDB for storage.

### 4. Install Dependencies
Install required Python libraries:
```bash
pip install -r requirements.txt
```

### 5. Start Streaming
- Run the Kafka producer (`producer.py`) to start sending news data.
- Execute the Spark streaming pipeline in Databricks to process and store the data.

## Project Structure
```plaintext
news-topic-project/
│
├── producer.py          # Kafka producer for streaming news data
├── consumer.py          # Kafka consumer for processing data
├── spark-stream.ipynb   # Databricks notebook for Spark Structured Streaming
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```


⭐️ **Enjoyed this project? Consider giving it a star on [GitHub](https://github.com/kunal356/news-topic-project)!**
