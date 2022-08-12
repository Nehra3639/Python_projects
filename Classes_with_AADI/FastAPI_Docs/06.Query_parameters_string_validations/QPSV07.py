# Required with Ellipsis (...)
# There's an alternative way to explicitly declare that a value is required.
# You can set the default parameter to the literal value ...:

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
