import uvicorn
from fastapi import FastAPI, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Category as CategoryModel, category
from app.schemas.category import Category, CategoryCreate

app = FastAPI(root_path="/api/v1")


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/categories")
async def get_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CategoryModel))
    return result.scalars().all()


@app.get("/categories/{id}")
async def get_category(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CategoryModel).where(CategoryModel.id == id))
    return result.scalar_one_or_none()


@app.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(payload: CategoryCreate, db: AsyncSession = Depends(get_db)):
    rusult = CategoryModel(name=payload.name, slug=payload.slug)
    db.add(rusult)
    await db.commit()
    await db.refresh(rusult)
    return rusult


def main():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
