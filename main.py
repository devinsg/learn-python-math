from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI(title="FastAPI Example", version="1.0")

# Define a request model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Path parameter example
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

# POST endpoint with JSON body
@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item.dict()
    }

# To run:
# uvicorn main:app --reload