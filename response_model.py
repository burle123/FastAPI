#Response Validation
#Hide Sensitive Data
#Data Transformation

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 12,
        "name": "Shantanu",
        "password": "SB"
    }

