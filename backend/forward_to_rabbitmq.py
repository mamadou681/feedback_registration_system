import pika
from credentials import password, username

# Getting rabbitmq credentials and its params

rabbitmq_credentials = pika.PlainCredentials(
    username=username, password=password)

params = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='rabbitmqvhost',
    credentials=rabbitmq_credentials,
)
MAINQUEUE = "messages_queue"

# Establish connection with rabbitmq and Send the data


def forward_to_queue(data):
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=MAINQUEUE, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=MAINQUEUE,
        body=data,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
        ),
    )
    connection.close()


if __name__ == "__main__":
    forward_to_queue()
