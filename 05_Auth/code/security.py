import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

Algo = os.getenv("ALGORITHM")
Key = os.getenv("SECRET_KEY")
Time_access = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password: str) -> str:
    passw = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passw, salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)