import os
import bcrypt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
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