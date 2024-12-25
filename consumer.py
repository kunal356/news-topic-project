from confluent_kafka import Consumer
from config import read_config

def configure_consumer():
    config = read_config()
    # sets the consumer group ID and offset  
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"

    # creates a new consumer instance
    consumer = Consumer(config)
    return consumer

def consume(topic):
  # subscribes to the specified topic
  consumer.subscribe([topic])

  try:
    while True:
      # consumer polls the topic and prints any incoming messages
      msg = consumer.poll(1.0)
      if msg is not None and msg.error() is None:
        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
  except KeyboardInterrupt:
    pass
  finally:
    # closes the consumer connection
    consumer.close()

if __name__ == "__main__":
  topic = "news-topic"
  consumer = configure_consumer()
  consume(topic=topic)