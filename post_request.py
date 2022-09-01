import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pdb
pdb.set_trace()
app = FastAPI(debug=True)


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    discount: float = None


@app.get("/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.discount:
        total = item.price - item.discount
        item_dict.update({"Total Amount": total})
    return item_dict


if __name__ == " __main__ ":
    uvicorn.run(app, host="127.0.0.1", port=8000)
