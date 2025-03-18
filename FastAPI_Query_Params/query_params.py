import uvicorn              # type: ignore
from fastapi import FastAPI # type: ignore 
app = FastAPI()

# try inputting http://localhost:8000/hello?name=Obie&age=23
@app.get("/hello")
async def hello(name: str, age: int):
    return {"name": name, "age": age}

if __name__ == "__main__":
    uvicorn.run("query_params:app", host="127.0.0.1", port=8000, reload=True)