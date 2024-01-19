from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from src.app.config import settings

from src.app.api.api_v1 import deps

#routers
from src.app.api.api_v1.account.router import router as account_router
from src.app.api.api_v1.profile.router import router as profile_router
from src.app.api.api_v1.product.router import router as product_router

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_router, prefix="/api/v1")
app.include_router(profile_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1/products")

@app.get("/")
async def root(db: Session = Depends(deps.get_db)):
    string = db.execute("SHOW TABLES").fetchall()
    return {"message": "Hello World", "db": string}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")