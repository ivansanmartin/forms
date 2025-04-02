from pika.adapters.asyncio_connection import AsyncioConnection
from dotenv import load_dotenv
from db.mongodb_manager import MongoDBManager
import asyncio
import os
import pika
import aiohttp
import time


load_dotenv()

async def init_mongodb():
    await MongoDBManager.create_connection(
        os.getenv("MONGODB_STRING_CONNECTION"), os.getenv("MONGODB_DATABASE")
    )
    
async def send_discord_notification(form):
    try:
        await asyncio.sleep(3)
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(form["discord_notification"]["webhook_url"], json={
                    "username": "Form Notification",
                    "embeds": [
                        {
                            "title": "Notification",
                            "description": f"A new answer has been submitted to: **{form['title']}**",
                            "color": 5763719
                        }
                    ]
                }) as response:

                    response_status = response.status
                    headers = response.headers

                    if response_status == 204:
                        print("[Discord] Notification sended.")
                        break

                    elif response_status == 429:
                        retry_after = float(headers.get("Retry-After", 0)) / 1000
                        print(f"Rate limit reached. Retrying in {retry_after:.2f} seconds...")
                        await asyncio.sleep(retry_after)
                    else:
                        response_text = await response.text()
                        print(f"Failed to send Discord notification: {response_status} - {response_text}")
                        break 

    except aiohttp.ClientError as err:
        print(f"Request error: {err}")

async def send_slack_notification(form):
    try:
        await asyncio.sleep(3)
        async with aiohttp.ClientSession() as session:
            async with session.post(form["slack_notification"]["webhook_url"], json={
                "text": f"A new answer has been submitted to: *{form['title']}*"
            }) as response:
                if response.ok:
                    print("[Slack] Notification sended.")

    except aiohttp.ClientError as err:
        return {"ok": False, "message": f"Request error: {err}", "status_code": 500}

async def send_notification(collection, form_id):
    form = await collection.find_one({"form_id": form_id})
    
    tasks = []

    if form:
        if "discord_notification" in form:
            tasks.append(send_discord_notification(form))

        if "slack_notification" in form:
            tasks.append(send_slack_notification(form))

    if tasks:
        await asyncio.gather(*tasks)


def callback(ch, method, properties, body):
    try:
        collection = MongoDBManager.get_collection(os.getenv("MONGODB_COLLECTION"))
        form_id = body.decode("utf-8")
        asyncio.get_running_loop().create_task(send_notification(collection, form_id))
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
        print("[RabbitMQ] Broker connection successfully")
        connection.channel(on_open_callback=on_channel_open)

    def on_channel_open(channel):
        print("[RabbitMQ] Channel opened")
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
