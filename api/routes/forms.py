from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.deps import get_db
from api.schemas.forms import FormFill, FormFillResponse
from api.db.repositories import create_form, get_template
from api.db.models import FormSubmission
from api.errors.base import AppError

router = APIRouter(prefix="/forms", tags=["forms"])


@router.post("/fill", response_model=FormFillResponse)
def fill_form(form: FormFill, db: Session = Depends(get_db)):
    if not get_template(db, form.template_id):
        raise AppError("Template not found", status_code=404)

    path = get_template(db, form.template_id).pdf_path

    submission = FormSubmission(**form.model_dump(), output_pdf_path=path)
    return create_form(db, submission)


