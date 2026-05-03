from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

#Depends():

# def common_logic():
#     return{
#         "Message":"Common Logic Executed Automatically!"
#     }

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return data


#Reusable Logic:

# def get_current_user():
#     return{
#         "Name":"Shantanu"
#     }

# @app.get("/Profile")
# def Profile(user = Depends(get_current_user)):
#     return user

# @app.get("/Dashboard")
# def Dashoard(user = Depends(get_current_user)):
#     return user

#Authentication:

def verify_token(token: str = Header(None)):
    
    if token!= "mysecrettoken":
        raise HTTPException(
            status_code = 401,
            detail = "Unauthorized User!" 
        )

    return{
        "User":"Authorized User!"
    }

@app.get("/secure_data")
def secure_data(user = Depends(verify_token)):
    return{
        "Message":"Secure Data Accessed!",
        "User": user
    }