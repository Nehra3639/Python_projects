# Query parameter list / multiple values with defaults
# And you can also define a default list of values if none are provided:

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items
