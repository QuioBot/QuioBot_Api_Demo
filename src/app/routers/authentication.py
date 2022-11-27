from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app import schemas, database, models, token
from app.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        print('Username Ghalat')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        print('Password Ghalat')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    print('Kulchi Mezian')
    access_token = token.create_access_token(data={"sub": user.email})

    print(user.name)

    return {"username":user, "access_token": access_token, "token_type": "bearer"}