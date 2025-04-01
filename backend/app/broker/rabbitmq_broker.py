import asyncio
import pika
import json
import os
from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exceptions import AMQPConnectionError

class RabbitMQ:
    """
    RabbitMQ: Async connection manager using pika's AsyncioConnection.

    Class Attributes:
      - _instance: Singleton instance.
      - _connection: Active AsyncioConnection.
      - _channel: Channel for publishing messages.
      - _loop: Current asyncio event loop.
    """
    _instance = None
    _connection = None
    _channel = None
    _loop = None

    @classmethod
    async def connect(cls):
        """
        Establish an asynchronous connection to RabbitMQ, open a channel,
        and declare the queue using environment variables.
        
        Returns:
            The singleton instance of RabbitMQ.
        """
        if cls._instance is not None and cls._channel and not cls._channel.is_closed:
            return cls._instance

        cls._loop = asyncio.get_running_loop()
        credentials = pika.PlainCredentials(
            username=os.getenv("RABBITMQ_USERNAME"),
            password=os.getenv("RABBITMQ_PASSWORD")
        )
        parameters = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=int(os.getenv("RABBITMQ_PORT")),
            virtual_host=os.getenv("RABBITMQ_VIRTUALHOST"),
            credentials=credentials,
            heartbeat=60
        )

        channel_future = cls._loop.create_future()

        def on_channel_open(channel):
            cls._channel = channel
            channel_future.set_result(channel)

        def on_connection_open(connection):
            connection.channel(on_open_callback=on_channel_open)

        def on_connection_open_error(connection, error):
            if not channel_future.done():
                channel_future.set_exception(error)

        try:
            cls._connection = AsyncioConnection(
                parameters,
                on_open_callback=on_connection_open,
                on_open_error_callback=on_connection_open_error,
            )
        except AMQPConnectionError as e:
            print(f"Failed to create AsyncioConnection: {e}")
            raise

        await channel_future

        declare_future = cls._loop.create_future()
        def on_queue_declared(frame):
            declare_future.set_result(True)

        cls._channel.queue_declare(
            queue=os.getenv("RABBITMQ_QUEUE"),
            callback=on_queue_declared
        )
        await declare_future

        print("Connected to RabbitMQ")
        cls._instance = cls()
        return cls._instance

    @classmethod
    async def send_message(cls, submitted, routing_key=None):
        """
        Publishes a JSON message to the RabbitMQ queue.
        Reconnects if the channel is closed.
        
        Args:
            submitted: An object with a model_dump_json() method that returns serializable data.
        """
        if cls._channel is None or cls._channel.is_closed:
            await cls.connect()

        cls._channel.basic_publish(
            exchange="",
            routing_key=routing_key,
            body=submitted
        )