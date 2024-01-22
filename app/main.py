from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



# Create a post method
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# Create Item model using Pydantic
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None



