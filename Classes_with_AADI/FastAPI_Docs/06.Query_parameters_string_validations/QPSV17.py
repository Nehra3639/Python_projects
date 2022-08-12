# Exclude from OpenAPI
# To exclude a query parameter from the generated OpenAPI schema (and thus,
# from the automatic documentation systems),
# set the parameter include_in_schema of Query to False:
from __future__ import annotations

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: str | None = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
