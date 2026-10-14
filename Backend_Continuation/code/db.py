from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

required_settings = {
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
}

missing = [
    name for name, value in required_settings.items()
    if not value
]

if missing:
    raise RuntimeError(
        f"Missing database configuration: {', '.join(missing)}"
    )

DB_PASSWORD = quote_plus(DB_PASSWORD)

DB_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DB_URL, echo=True) #create an engine to maintain a lowlevel connection pool to DB, echo allows us to do logging 

SessionLocal = sessionmaker(
    bind=engine,                       #the session to the DB
    autocommit=False,                  #makes sure changes are not automatically committed to the DB
    autoflush=False                    #explicit control over flushin
)
#session maker allows to generate individual session 

Base = declarative_base()
#to return a base class for our models to inherit from

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()