import pika
import json
from server.database import products_coll
from server.serializers.product_serializer import product_serializer_noid


def on_msg_recv(ch, method, properties, body):
    print(f"FastAPI Consumer - Received A New Message!")
    data = json.loads(body)
    print("BRUHHHHHH idddddd", data)

    if properties.content_type == "product_created":
        ser_data = product_serializer_noid(data)
        products_coll.insert_one(ser_data)
        print("FastAPI Consumer - Created A Product!")

    elif properties.content_type == "product_updated":
        ser_data = product_serializer_noid(data)
        products_coll.update_one(
            {"id": data["id"]}, {"$set": ser_data}, upsert=True
        )
        print("FastAPI Consumer - Updated A Product!")

    elif properties.content_type == "product_deleted":
        products_coll.delete_one({"id": data})
        print("FastAPI Consumer - Deleted A Product!")


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
# channel.close()
