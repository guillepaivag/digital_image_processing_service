from fastapi import FastAPI
from src.routes import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/")
async def read_root():
    return "Buenos dias"