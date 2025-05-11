import uvicorn
from api.db.database import init_db
from fastapi import FastAPI, status
from api.core.settings import settings
from api.v1.routes import api_version_one
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server is shuting down...")


app = FastAPI(
    version="1.0.0",
    lifespan=life_span,
    title="Book CRUD Project",
    description="A book APIs that allows CRUD operations",
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/", tags=["Home"], status_code=status.HTTP_200_OK)
async def get_root():
    return JSONResponse(content={"message": "Welcome to Book Project APIs"})


app.include_router(api_version_one)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=settings.PORT, reload=True)
