from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
def get_name(name:str=None):
    return {"Name":name}            # http://127.0.0.1:8000/users?name=SB

@app.get("/Product")
def get_product(limit: int = 100):
    return {"Limit": limit}      # http://127.0.0.1:8000/Product?limit=100

@app.get("/items")
def get_items(name: str = None,price : int =0):
    return {"Name": name, "Price": price}    # http://127.0.0.1:8000/items?name=John&price=10