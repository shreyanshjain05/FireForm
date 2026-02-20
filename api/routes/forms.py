from fastapi import APIRouter
from api.schemas.forms import FormFill
from api.schemas.common import SuccessResponse
# from src.fill_document import name_of_function_that_fills_document

router = APIRouter(prefix="/forms", tags=["forms"])


@router.post("/fill", response_model=SuccessResponse)
def fill_form(form_fill: FormFill):
    return SuccessResponse(
        data=form_fill,
        success=True
    )
    # return name_of_function_that_fills_document()