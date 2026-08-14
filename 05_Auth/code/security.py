from pwdlib import PasswordHash
import bcrypt
import os
from dotenv import load_dotenv
from pwdlib import PasswordHash
from pydantic import BaseModel, Field
os.load_dotenv()

Algo = os.getenv("ALGORITHM")
Key = os.getenv("SECRET_KEY")
Time_access = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password: str) -> str:
    salt = bcry