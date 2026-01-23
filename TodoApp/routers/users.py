from typing import Annotated

from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Todos, Users
from database import SessionLocal
from .auth import get_current_user, bcrypt_context
from .todos import TodoRequest

router = APIRouter(
    prefix='/users',
    tags=['users']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class ChangeUserPassRequest(BaseModel):
    password: str

@router.get("/get-user-info")
async def get_user_info(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    requested_user = db.query(Users).filter(Users.id == user.get(id)).first()
    if requested_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return requested_user

@router.put("/change-user-pass")
async def change_user_pass(user: user_dependency, db: db_dependency, change_user_pass_request: ChangeUserPassRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    requested_user = db.query(Users).filter(Users.id == user.get(id)).first()
    if requested_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    requested_user.hashed_password = bcrypt_context.hash(change_user_pass_request.password)
    db.add(requested_user)
    db.commit()







