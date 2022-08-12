# Required with None
# You can declare that a parameter can accept None, but that it's still required.
# This would force clients to send a value, even if the value is None.
#
# To do that, you can declare that None is a valid type but still use default=...:
from __future__ import annotations

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
