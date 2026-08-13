from app.models.base import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Category(BaseModel):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"<Category id={self.id} name={self.name} prefix={self.slug}>"
