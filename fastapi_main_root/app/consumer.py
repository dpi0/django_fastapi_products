import pika
import json
from server.database import products_coll
from server.serializers.product_serializer import product_serializer_noid


def on_msg_recv(ch, method, properties, body):
    print(f"FastAPI Consumer - Received A New Message!")
    data = json.loads(body)

    if properties.content_type == "product_created":
        ser_data = product_serializer_noid(data)
        products_coll.insert_one(ser_data)
        print("Product Created")

    elif properties.content_type == "product_updated":
        print("Product Updated")

    elif properties.content_type == "product_deleted":
        print("Product Deleted")


conn_params = pika.URLParameters(
    "amqps://szqbwjyt:z9rwVNxUAsohWlpZp4WpYdNJieD4k_up@octopus.rmq3.cloudamqp.com/szqbwjyt"
)


conn = pika.BlockingConnection(conn_params)
channel = conn.channel()

channel.queue_declare(queue="django_admin_queue")

channel.basic_consume(
    queue="django_admin_queue",
    on_message_callback=on_msg_recv,
    auto_ack=True,
)

print("FastAPI Consumer - Started Consuming...")
channel.start_consuming()
channel.close()
