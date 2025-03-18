from fastapi import FastAPI #type: ignore
app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

# this will store the name parameter
# that you're passing 
@app.get("/hello/{name}")
async def hello(name):
    return {"name": name}

# # you can have multiple parameters separated by "/"
# # symbol
# @app.get("/hello/{name}/{age}")
# async def hello(name, age):
#     return {"name": name, "age": age}

# path parameters with types
@app.get("/hello/{name}/{age}")
async def hello(name: str, age: int):
    return {"name": name, "age": age}