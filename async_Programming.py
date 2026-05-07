# import time 
# import asyncio

# #Synchronous function
# def sync_function():
#     print("Starting synchronous function...")
#     time.sleep(2)  # Simulate a time-consuming task
#     print("Synchronous function completed.")

# sync_function()  # Call the synchronous function

# #Asynchronous function
# async def async_function():
#     print("Starting asynchronous function...")
#     await asyncio.sleep(2)  # Simulate a time-consuming task
#     print("Asynchronous function completed.")

# # Run the asynchronous function
# asyncio.run(async_function())


import time
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }

# O/P - It will load the message in three sec