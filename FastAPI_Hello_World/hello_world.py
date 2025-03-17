from fastapi import FastAPI

# declare an application object of FastAPI class
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
