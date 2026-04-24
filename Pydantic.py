from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     city:str

# @app.post("/create_user")

# def create_user(user: User):
#     return{"Message": "user created successfully!",
#            "data":user}  

#Nested Pydantic Models

class Address(BaseModel):
    city:str
    pin:int                      #Bydefault int value is 0

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user") 

def create_user(user:User):
    return user