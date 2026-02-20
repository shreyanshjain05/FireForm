from fastapi import HTTPException, status

class APIError(HTTPException):
    def __init__(self, status_code: int, code: str, message: str):
        super().__init__(
            status_code=status_code,
            detail={
                "success": False,
                "error": {"code": code, "message": message}
            }
        )

def not_found(entity: str):
    return APIError(status_code=status.HTTP_404_NOT_FOUND,
                    code=f"{entity.upper()}_NOT_FOUND",
                    message=f"{entity} not found")

def bad_request(message: str):
    return APIError(status_code=status.HTTP_400_BAD_REQUEST,
                    code="BAD_REQUEST", message=message)