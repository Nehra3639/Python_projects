# Query parameter list / multiple values
# When you define a query parameter explicitly with Query you can also declare it
# to receive a list of values, or said in other way, to receive multiple values.

# For example, to declare a query parameter q that can appear
# multiple times in the URL, you can write:
from __future__ import annotations

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items
