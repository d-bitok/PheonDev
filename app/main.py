from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Development with FastAPI"}

@app.get("/new")
async def root():
    return {"message": "New API Development Page"}