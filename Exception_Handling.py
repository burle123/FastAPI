from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, user_name: str):
        self.user_name = user_name

@app.get("/user/{user_name}")
def get_user(user_name : str):
    if user_name != "Shantanu":
        raise UserNotFoundException(user_name)
    return{
        "id":1,
        "name":"Shantanu"
    }

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException): #Global Exception Handler
    return JSONResponse(
        status_code=404,
        content={"message": f"User {exc.user_name} not found"}
    )


# @app.get("/user/{user_id}")
# def get_user(user_id : int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )
#     return{
#         "id":1,
#         "name":"Shantanu"
#     }