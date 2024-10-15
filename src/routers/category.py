from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.backend.db_depends import get_db
from typing import Annotated

from src.models import *
from sqlalchemy import insert  
from src.schemas.schemas import CreateCategory

from slugify import slugify


router = APIRouter(prefix='/category', tags=['category'])


@router.get('/all_categories')
async def get_all_categories():
    pass


@router.post('/create')
async def create_category(db: Annotated[Session, Depends(get_db)], create_category: CreateCategory):
    db.execute(insert(Category).values(
        name=create_category.name,
        slug=slugify(create_category.name),
        parent_id=create_category.parent_id))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }



@router.put('/update_category')
async def update_category():
    pass


@router.delete('/delete')
async def delete_category():
    pass