from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from app.hashing import Hash


def create(request: schemas.User, db: Session):
    user = db.query(models.User).filter(
        models.User.name== request.name).first()

    email = db.query(models.User).filter(
        models.User.email== request.email).first()


    if  user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User Name Already Taken")

    if  email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Email Already Taken")

    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
