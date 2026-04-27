from fastapi import FastAPI, status, HTTPException
app = FastAPI()

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"User Created!!"
    }

@app.get("/user")
def get_user():
    return{
        "status" : "Success!",
        "msg" : "User Fetched",
        "data":{
            "name": "Shantanu",
            "age":22
        }
    }



        