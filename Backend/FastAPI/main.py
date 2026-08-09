from fastapi import FastAPI
from routers import products, basic_auth_users, jwt_auth_users, users, users_db
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.include_router(products.router)

app.include_router(users.router)

app.include_router(basic_auth_users.router)

app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Url local: http://127.0.0.1:8000

@app.get("/") # type: ignore
async def root():
    return "Hola FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url") # type: ignore
async def url():
    return {"url": "https://mouredev.com/python"}

# Inicia el server: uvicorn main:root --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc