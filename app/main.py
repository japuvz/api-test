from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}


# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# Create Item model using Pydantic

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# create main method that starts up app using uvicorn
    


