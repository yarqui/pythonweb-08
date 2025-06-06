from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import date


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = EmailStr
    phone_number: str | None = Field(max_length=20, default=None)
    birthday: date | None = None
