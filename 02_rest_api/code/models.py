from pydantic import BaseModel, field_validator

class Book(BaseModel):
    id: int
    name: str
    author: str
    publisher: str
    price: float
    days_Borrowed: int

    @field_validator('price')
    def check_price(cls, price):
        if price <= 0:
            raise ValueError('Price cannot be 0 and less')
        return price

    @field_validator("days_Borrowed")
    def check_days(cls, Days):
        if Days <= 0:
            raise ValueError('Days borrowed must be greater than 0')
        return Days