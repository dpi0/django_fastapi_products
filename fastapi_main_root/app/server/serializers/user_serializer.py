def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "product_id": user["product_id"],
    }


def user_list_serializer(users) -> list:
    return [user_serializer(user) for user in users]
