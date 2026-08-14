from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr

class UserCreate(UserBase):
    Password: str 

class UserResponse(UserBase):
    U_ID: int

    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    BookName: str
    Author: str
    Publisher: str
    Price: float = Field(..., ge=0.0)
    Quantity: int = Field(..., ge=0)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    BookName: Optional[str] = None
    Author: Optional[str] = None
    Publisher: Optional[str] = None
    Price: Optional[float] = Field(None, ge=0.0)
    Quantity: Optional[int] = Field(None, ge=0)

class BookResponse(BookBase):
    B_ID: int

    model_config = ConfigDict(from_attributes=True)