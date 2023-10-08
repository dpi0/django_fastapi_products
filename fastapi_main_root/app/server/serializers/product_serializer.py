def product_serializer(product) -> dict:
    return {
        "_id": product["_id"],
        "id": product["id"],
        "name": product["name"],
        "image": product["image"],
        "likes": product["likes"],
    }


def product_serializer_noid(product) -> dict:
    return {
        # "_id": product["_id"],
        "id": product["id"],
        "name": product["name"],
        "image": product["image"],
        "likes": product["likes"],
    }


def product_list_serializer(products) -> list:
    return [product_serializer(product) for product in products]
