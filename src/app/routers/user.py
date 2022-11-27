from fastapi import APIRouter
from src.app import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.app.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)



@router.get("/whoami", response_model=schemas.UserOutSchema, dependencies=[Depends(oauth2.get_current_user_1)])
async def read_users_me(current_user: schemas.UserOutSchema = Depends(oauth2.get_current_user_1) , db: Session = Depends(get_db)):
    return current_user