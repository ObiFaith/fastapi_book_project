import uvicorn
from fastapi import FastAPI, status
from api.v1.routes import api_version_one
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  version='1.0.0',
  title='Book CRUD Project',
  description='A book APIs that allows CRUD operations',
)

origins = [
  'http://localhost:3000',
  'http://localhost:5173',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
  allow_headers=['*'],
)

@app.get('/', tags=["Home"], status_code=status.HTTP_200_OK)
async def get_root():
  return JSONResponse(content={
    "message": "Welcome to Book Project APIs"
  })

app.include_router(api_version_one)

if __name__ == '__main__':
  uvicorn.run(app='main:app', port=7001, reload=True)
