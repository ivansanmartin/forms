import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.connection import ConnectionParameters
from pika.credentials import PlainCredentials

class RabbitMQ():
    channel: BlockingChannel = None
     
    
    @staticmethod
    def create_connection(connection_parameters: ConnectionParameters) -> BlockingChannel:
        connection = pika.BlockingConnection(connection_parameters)
        print("[RabbitMQ] Broker connection succesfully")
        RabbitMQ.channel = connection.channel()
        
        return RabbitMQ.channel
    
    @staticmethod
    def get_channel() -> BlockingChannel:
        return RabbitMQ.channel