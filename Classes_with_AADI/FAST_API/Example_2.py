from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stud_db = []


class Student(BaseModel):
    std_name: str
    fthr_name: str
    mthr_name: str
    education: str
    total_marks: int
    percent_marks: float


@app.get("/")
def get_msg():
    return {"message": "Welcome to Cambridge University"}


@app.get("/items/{item_id}")
def std_name():
    return
