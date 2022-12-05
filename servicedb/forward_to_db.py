import pika
import json

from credentials import Credentials
import services as _services

# Getting rabbitmq credentials and its params
rabbitmq_credentials = pika.PlainCredentials(
    username=Credentials.username, password=Credentials.password)

params = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='rabbitmqvhost',
    credentials=rabbitmq_credentials,
)
MAINQUEUE = "messages_queue"

# Fetch data from rabbitmq and send it to db using create_userinfo function


async def fetch_from_rabbitmq(db):
    def on_message(channel, method_frame, header_frame, body):
        print(method_frame.delivery_tag)
        userinfo = body.decode("utf-8")
        userinfo = json.loads(userinfo)
        _services.create_userinfo(db, userinfo=userinfo)
        print(userinfo)
        print()
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_consume(MAINQUEUE, on_message)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
