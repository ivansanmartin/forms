from broker.rabbitmq_broker import RabbitMQ
import pika
import os
from dotenv import load_dotenv

load_dotenv()

def start_rabbitmq():
    credentials = pika.PlainCredentials(username=os.getenv("RABBITMQ_USERNAME"), password=os.getenv("RABBITMQ_PASSWORD"))
    connection_parameters = pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST"), port=os.getenv("RABBITMQ_PORT"), virtual_host=os.getenv("RABBITMQ_VIRTUALHOST"), credentials=credentials)
    channel = RabbitMQ.create_connection(connection_parameters)
    channel.queue_declare(os.getenv("RABBITMQ_QUEUE"))
    
    return channel
    
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    
    
if __name__ == "__main__":
    channel = start_rabbitmq()
    channel.basic_consume(queue=os.getenv("RABBITMQ_QUEUE"), auto_ack=True, on_message_callback=callback)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()