from fastapi import APIRouter
from api.schemas.templates import TemplateCreate
from api.schemas.common import SuccessResponse

router = APIRouter(prefix="/templates", tags=["templates"])

@router.post("/create", response_model=SuccessResponse)
def create(template: TemplateCreate):
    return SuccessResponse(
        data=template,
        success=True
    )
    # return create_template(template)