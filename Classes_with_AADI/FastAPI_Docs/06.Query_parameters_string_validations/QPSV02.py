# Use Query as the default value
# And now use it as the default value of your parameter,
# setting the parameter max_length to 50:
from __future__ import annotations

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
