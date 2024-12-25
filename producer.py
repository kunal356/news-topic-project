import csv
import random
from confluent_kafka import Producer
from config import read_config

def configure_producer():
    config = read_config()
    return Producer(config)

def produce_from_csv(topic:str, producer:Producer, file_path:str):
    """
        Selects a random news topic from a dataset and publishes it to a specified Kafka topic.

    Args:
        kafka_topic (str): The name of the Kafka topic to publish the news topic to.
        producer (Producer): An instance of Confluent Kafka Producer.
        file_path (str): The file path to the dataset containing news topics.
        file_type (Optional[str], optional): The type of the dataset file ('csv', 'json'). 
            If not provided, the function will infer the type based on the file extension.
            Defaults to None.
        encoding (str, optional): The encoding of the dataset file. Defaults to 'utf-8'.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = list(csv.DictReader(file))
            total_rows = len(reader)

            print(f"Total rows in CSV: {total_rows}")
            
            # Produce random rows
            random_row = random.choice(reader)
            key = str(random_row.get('ID', '0'))
            value = str(random_row)
            producer.produce(topic=topic, key=key, value=value)
            print(f"Produced message: key ={key}, value={value}")
            
            producer.flush()
    except Exception as e:
        print(f"Error producing messages: {e}")

if __name__ == "__main__":
    topic = "news-topic"
    csv_file_path = "data/bbc_news.csv"
    producer = configure_producer()
    try:
        while True:
            print("Press Crl+C to stop the producer...")
            produce_from_csv(topic=topic, producer=producer, file_path=csv_file_path)
    except KeyboardInterrupt:
        pass
    finally:
        # Closing producer
        producer.flush()
        print("Stopping Producer")
    