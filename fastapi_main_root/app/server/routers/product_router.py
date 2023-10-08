from fastapi import APIRouter, status, HTTPException, Response, Depends
from fastapi.encoders import jsonable_encoder
from typing import List
from ..database import products_coll
from ..serializers.product_serializer import (
    product_serializer,
    product_list_serializer,
    product_serializer_noid,
)
from bson.objectid import ObjectId
from typing import Union, Any, Optional
from ..models import GetProduct, LikeProduct
from .producer import publish


class Helper:
    def __init__(self) -> None:
        pass

    def validate_id(self, product_id: str) -> bool:
        if ObjectId.is_valid(product_id):
            return True
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid Product ID: {product_id}",
        )

    def find_product(self, product_id: str) -> Any:
        return products_coll.find_one({"_id": ObjectId(product_id)})

    # def find_product(self, product_name: str) -> Any:
    #     return products_coll.find_one({"name": product_name})

    def validate_product(self, product_id: str) -> bool:
        found_product = self.find_product(product_id)
        if found_product:
            return True

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product Not Found",
        )


router = APIRouter()
helper = Helper()


@router.get(
    "/",
    response_description="Get All Products",
    response_model=List[GetProduct],
)
async def get_all_products() -> list[dict[str, str]]:
    # skip: int = (page - 1) * limit
    products: list[dict[str, str]] = product_list_serializer(
        products_coll.find()
    )
    return products


@router.get(
    "/{product_id}",
    description="Get Product",
    response_model=GetProduct,
)
async def get_post(
    product_id: str,
) -> dict[str, str] | None:
    helper.validate_id(product_id)
    if helper.validate_product(product_id):
        product = helper.find_product(product_id)
        return product_serializer(product)


@router.put(
    "/{product_id}/like",
    description="Like Product",
    response_model=GetProduct,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_202_ACCEPTED,
)
async def like_product(product_id: str) -> dict[str, str] | None:
    if helper.validate_product(product_id):
        products_coll.update_one(
            {"_id": ObjectId(product_id)},
            {"$inc": {"likes": 1}},
        )
        product = product_serializer_noid(helper.find_product(product_id))
        publish("liked_product", product)
        return product
