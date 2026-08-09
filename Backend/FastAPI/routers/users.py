from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Santiago", surname="Rivera", url="http://rivera.dev", age=21),
    User(id=2, name="Sinsinati", surname="Dev", url="https://sinsinatidev.com", age=35),
    User(id=3, name="Irai", surname="Rigoberto", url="https://irei.com", age=20),
]

@router.get("/usersjson")
async def usersjson():
    return [
        {"name": "Santiago", "surname": "Rivera", "url": "https://rivera.dev", "age": 21},
        {"name": "Sinsinati", "surname": "Dev", "url": "https://sinsinatidev.com", "age": 35},
        {"name": "Irai", "surname": "Rigoberto", "url": "https://irei.com", "age": 20},
    ]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")  # Path
async def user_id(id: int):
    return search_user(id)

@router.get("/user/")  # Query
async def user(id: int):
    return search_user(id)

@router.post("/user/")
async def user_post(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user

@router.put("/user/")
async def user_put(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user

@router.delete("/user/{id}")
async def user_delete(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except Exception:
        return {"error": "No se ha encontrado el usuario"}