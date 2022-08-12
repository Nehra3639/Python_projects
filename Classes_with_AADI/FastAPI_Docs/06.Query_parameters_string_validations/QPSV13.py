# Declare more metadata
# You can add more information about the parameter.
# That information will be included in the generated OpenAP and used by the
# documentation user interfaces and external tools.

# You can add a title:

from __future__ import annotations

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
        q: str | None = Query(default=None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


