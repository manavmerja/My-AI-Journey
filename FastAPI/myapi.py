from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


students = {
    1: {"name": "John", "age": 20},
    2: {"name": "Jane", "age": 22},
    3: {"name": "Bob", "age": 21}
}

class Student(BaseModel):
    name: str
    age: int
    gender: str



@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student to retrieve", gt=1, lt=100)):
    return students.get(student_id) 


@app.get("/get-by-name")
def get_student_by_name(name: str = Query(..., description="The name of the student to retrieve")):
    for student in students.values():
        if student["name"] == name:
            return student
    return {"error": "Student not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    
    students[student_id] = student.model_dump()
    return students[student_id]
