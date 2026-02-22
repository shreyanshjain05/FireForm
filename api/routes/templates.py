from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.deps import get_db
from api.schemas.templates import TemplateCreate, TemplateResponse
from api.db.repositories import create_template
from api.db.models import Template
from api.errors.base import AppError

router = APIRouter(prefix="/templates", tags=["templates"])

@router.post("/create", response_model=TemplateResponse)
def create(template: TemplateCreate, db: Session = Depends(get_db)):
    tpl = Template(**template.model_dump())
    return create_template(db, tpl)