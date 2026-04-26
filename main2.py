from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    city:str

@app.post("/create_user")

def create_user(user: User):
    return{"Message": "user created successfully!",
           "data":user} 

@app.put("/update_user/{user_id}")
def update_user(user_id:int, user:User, notify:bool=False):
    return {
        "msg":"User updated successfully!",
        "notify":notify,
        "data" :user
    }