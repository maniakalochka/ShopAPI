from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    stock: int
    category: int


class CreateCategory(BaseModel):
    name: str
    parent_id: int | None


