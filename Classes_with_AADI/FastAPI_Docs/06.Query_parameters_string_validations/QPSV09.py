# Use Pydantic's Required instead of Ellipsis (...)
# If you feel uncomfortable using ..., you can also import and use Required from Pydantic:

from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results