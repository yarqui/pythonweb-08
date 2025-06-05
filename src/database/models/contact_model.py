from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column

from base_model import IDOrmModel


class Contact(IDOrmModel):
    __tablename__ = "contacts"

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    phone_number: Mapped[str] = mapped_column(String(20))
    birthday: Mapped[date] = mapped_column(Date)
