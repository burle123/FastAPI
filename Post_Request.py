from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
# def create_user(name: str, age: int):
#     return {"Name": name, "Age": age}   #Test in swagger UI with JSON body: {"name": "Alice", "age": 30}

def create_user(user: dict):
    return{"User": user}   # To send multiple data in JSON format, we can use a dictionary. Test in swagger UI with JSON body: {"name": "Alice", "age": 30}
                        #By using this method url will not change it remains the same http://127.0.0.1:8000/docs#/default/create_user_create_user_post