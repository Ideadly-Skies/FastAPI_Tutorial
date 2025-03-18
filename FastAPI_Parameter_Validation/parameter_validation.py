import uvicorn #type: ignore
from fastapi import FastAPI, Path, Query #type: ignore
app = FastAPI()

# string too long or too short
@app.get("/hello/{name}")
async def hello(name:str=Path(..., min_length=3, max_length=10)):
    return {"name": name}

# get name and age as paths (with input validation in here)
# and percent as query 
@app.get("/hello/{name}/{age}")
async def hello(*, name: str=Path(..., min_length=3, max_length=10), \
                age: int = Path(..., ge=1, le=100), \
                percent: float = Query(..., ge=0, le=100)):
    return {"name": name, "age": age}

# checks if the current script is being run directly as the main program
if __name__ == "__main__":
    uvicorn.run("parameter_validation:app", host="127.0.0.1", port=8000, reload=True)