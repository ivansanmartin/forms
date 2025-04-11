from pika.adapters.asyncio_connection import AsyncioConnection
from dotenv import load_dotenv
from db.mongodb_manager import MongoDBManager
import asyncio
import os
import pika

load_dotenv()

async def init_mongodb():
    await MongoDBManager.create_connection(
        os.getenv("MONGODB_STRING_CONNECTION"), os.getenv("MONGODB_DATABASE")
    )
    
async def update_metrics(form):
    pass

def callback(ch, method, properties, body):
    try:
        collection = MongoDBManager.get_collection(os.getenv("MONGODB_COLLECTION"))
        form_id = body.decode("utf-8")
        asyncio.get_running_loop().create_task(update_metrics(collection, form_id))
    except Exception as e:
        print(f"Error processing message: {e}")

async def init_listen_rabbitmq():
    credentials = pika.PlainCredentials(
        username=os.getenv("RABBITMQ_USERNAME"),
        password=os.getenv("RABBITMQ_PASSWORD")
    )
    
    connection_parameters = pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST"),
        port=int(os.getenv("RABBITMQ_PORT")),
        virtual_host=os.getenv("RABBITMQ_VIRTUALHOST"),
        credentials=credentials
    )

    def on_connection_open(connection):
        print("[RabbitMQ - Metrics] Broker connection successfully")
        connection.channel(on_open_callback=on_channel_open)

    def on_channel_open(channel):
        print("[RabbitMQ - Metrics] Channel opened")
        channel.queue_declare(queue=os.getenv("RABBITMQ_QUEUE"))
        channel.basic_consume(
            queue=os.getenv("RABBITMQ_QUEUE"),
            auto_ack=True,
            on_message_callback=callback 
        )
    
    AsyncioConnection(
        connection_parameters, on_open_callback=on_connection_open
    )

    await asyncio.Future()

async def main():
    await init_mongodb()
    await init_listen_rabbitmq()

if __name__ == "__main__":
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        exit()
    except:
        print("Unable to perform Action")
