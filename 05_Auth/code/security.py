import os
import bcrypt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import jwt

load_dotenv()

Algo = os.getenv("ALGORITHM")
Key = os.getenv("SECRET_KEY")
TIME_EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password: str) -> str:
    passw = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passw, salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=TIME_EXPIRE
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        Key,
        algorithm=Algo
    )
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db)
# ):
#     try:
#         payload = jwt.decode(
#             token,
#             Key,
#             algorithms=[Algo]
#         )
#         user_id = payload.get("sub")
#         if user_id is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid authentication credentials"
#             )
#     except jwt.InvalidTokenError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials"
#         )
#     user = crud.get_user_by_id(db, int(user_id))
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="User not found"
#         )
#     return user