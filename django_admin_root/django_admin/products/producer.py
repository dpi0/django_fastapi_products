import pika, json

# from pika.exchange_type import ExchangeType

conn_params = pika.URLParameters(
    "amqps://szqbwjyt:z9rwVNxUAsohWlpZp4WpYdNJieD4k_up@octopus.rmq3.cloudamqp.com/szqbwjyt"
)

conn = pika.BlockingConnection(conn_params)
channel = conn.channel()


channel.queue_declare(queue="django_admin_queue")

# MSG: str = "sent to fastapi"


def publish(msg, data):
    props = pika.BasicProperties(msg)
    channel.basic_publish(
        exchange="",
        routing_key="django_admin_queue",
        body=json.dumps(data),
        properties=props,
    )

    # print(f"Sent message: {MSG}")


# publish()

# conn.close()
