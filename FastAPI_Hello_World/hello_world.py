from fastapi import FastAPI

# declare an application object of FastAPI class
# invoke with the command: uvicorn "FastAPI_Hello_World.hello_world:app" --reload
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}