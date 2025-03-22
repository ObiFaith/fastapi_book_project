from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def success_response(status_code: int, message: str, data: Optional[dict] = None):
  """Returns a JSON response for success responses"""

  response_data = {
    "status": "success",
    "status_code": status_code,
    "message": message,
    "data": data or {}
  }

  return JSONResponse(
    status_code=status_code,
    content=jsonable_encoder(response_data)
  )

def error_response(status_code: int, message: str, data: Optional[dict] = None):
  """Returns a JSON response for error responses"""

  response_data = {
    "status": "error",
    "status_code": status_code,
    "message": message,
    "data": data or {}
  }

  return JSONResponse(
    status_code=status_code,
    content=jsonable_encoder(response_data)
  )
