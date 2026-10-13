from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
import jwt
from books import router as books_router
import models
import schemas
import crud
from db import engine, get_db
from dependencies import get_current_user
from auth import router as auth_router
from security import (
    hash_password,
    verify_password,
    create_access_token,
    Algo,
    Key
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            Key,
            algorithms=[Algo]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user = crud.get_user_by_id(db, int(user_id))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user



app = FastAPI(title="Library Management API")
app.include_router(books_router)

@app.post("/auth/register",
          response_model=schemas.UserResponse,
          status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db), ):
    existing_user = crud.get_user_by_email(db, user.Email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)

@app.post("/auth/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db, form_data.username)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    if not verify_password(form_data.password, db_user.PasswordHash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    access_token = create_access_token(
        data={"sub": str(db_user.U_ID)}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
