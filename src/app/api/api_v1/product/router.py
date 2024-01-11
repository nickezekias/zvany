from fastapi import APIRouter

router = APIRouter(
    tags=["product"]
)

@router.get("/test", status_code=200)
async def test():
    return "Products Module Working"
