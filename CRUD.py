from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
todos = []

class ToDo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.post("/todos")
def create_todo(todo: ToDo):
    todos.append(todo)
    return {"message": "ToDo created successfully!", "todo": todo}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.get("/todos/{todo_id}")        #To get specific todo by id.
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "ToDo not found!"}