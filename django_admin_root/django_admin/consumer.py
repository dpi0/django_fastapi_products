import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


# from products.serializers import ProductSerializer
from products.models import Product

# from products.views import ProductViewSet


def on_msg_recv(ch, method, properties, body):
    print(f"Django Consumer - Received A New Message!")
    data = json.loads(body)

    if properties.content_type == "liked_product":
        # ser_data = product_serializer(data)
        # collection.insert_one(ser_data)
        print("Django Consumer - RECIEVED A Product!")
        print(data)
        print(data["id"])
        product_id = data["id"]
        # ProductViewSet.update_product(product_id)
        product = Product.objects.get(id=product_id)
        product.likes += 1
        product.save()
        print(
            f"Likes Updated of product id: {product_id} to likes --> {product.likes}"
        )


conn_params = pika.URLParameters(
    "amqps://szqbwjyt:z9rwVNxUAsohWlpZp4WpYdNJieD4k_up@octopus.rmq3.cloudamqp.com/szqbwjyt"
)

conn = pika.BlockingConnection(conn_params)
channel = conn.channel()

channel.queue_declare(queue="fastapi_main_queue")

channel.basic_consume(
    queue="fastapi_main_queue",
    on_message_callback=on_msg_recv,
    auto_ack=True,
)

print("Django Consumer - Started Consuming...")
channel.start_consuming()
channel.close()
