import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.connection import ConnectionParameters
import pika.exceptions
import time

class RabbitMQ():
    channel: BlockingChannel = None
     
    
    @staticmethod
    def create_connection(connection_parameters: ConnectionParameters) -> BlockingChannel:
        while True:
            try:
                connection = pika.BlockingConnection(connection_parameters)
                print("[RabbitMQ] Broker connection succesfully")
                RabbitMQ.channel = connection.channel()
        
                return RabbitMQ.channel
            except pika.exceptions.AMQPChannelError:
                print("[RabbitMQ] Waiting for reconnecting")
                time.sleep(5)
    
    @staticmethod
    def get_channel() -> BlockingChannel:
        return RabbitMQ.channel