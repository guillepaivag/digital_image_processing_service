from fastapi import FastAPI
from src.routes import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI1"}

def main(request):
    return {"message": "Hello from FastAPI2"}
