from app.models.base import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    login: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, login={self.login})"
