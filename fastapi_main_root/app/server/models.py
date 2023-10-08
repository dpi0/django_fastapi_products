from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    PlainSerializer,
    AfterValidator,
    WithJsonSchema,
    ConfigDict,
)
from datetime import datetime
from typing import Optional, Annotated, Union, Any
from bson.objectid import ObjectId


class ProductBase(BaseModel):
    name: str = Field(...)
    image: str = Field(...)
    likes: int = Field(...)


class GetProduct(ProductBase):
    pass


class LikeProduct(BaseModel):
    likes: int = Field(...)
