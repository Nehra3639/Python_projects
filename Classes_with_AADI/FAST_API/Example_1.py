from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = []


class Course(BaseModel):
    name: str
    id: int
    price: float


@app.get("/")
async def read_root():
    return {"Greeting": "Welcome to Book World"}


@app.get("/courses")
async def get_courses():
    return fake_db


@app.get("/courses/{course_id}")
async def get_a_course(course_id: int):
    course = course_id - 1
    return fake_db[course]


@app.post("/courses")
async def add_course(course: Course):
    fake_db.append(course.dict())
    return fake_db[-1]


@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    fake_db.pop(course_id - 1)
    return {"task": "deletion successful"}
