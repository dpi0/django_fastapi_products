import pika
import json

# from pika.exchange_type import ExchangeType

conn_params = pika.URLParameters(
    "amqps://szqbwjyt:z9rwVNxUAsohWlpZp4WpYdNJieD4k_up@octopus.rmq3.cloudamqp.com/szqbwjyt"
)

conn = pika.BlockingConnection(conn_params)
channel = conn.channel()


channel.queue_declare(queue="fastapi_main_queue")

# MSG: str = "sent to fastapi"


def publish(msg, data):
    props = pika.BasicProperties(msg)
    channel.basic_publish(
        exchange="",
        routing_key="fastapi_main_queue",
        body=json.dumps(data),
        properties=props,
    )

    # print(f"Sent message: {MSG}")


# data: dict = {"key1": "value1"}

# publish("first message", data=data)
# publish("first message", data=data)
# publish("first message", data=data)
# publish("first message", data=data)
# publish("first message", data=data)
# publish("first message", data=data)
# publish("first message", data=data)


# publish()

# conn.close()
