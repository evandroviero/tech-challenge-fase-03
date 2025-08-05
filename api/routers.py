from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/houses",
    tags=["houses"],
)


@router.get("/")
def get_houses():
    return {
        "houses": [
            {"id": 1, "address": "123 Main St", "price": 250000},
            {"id": 2, "address": "123 Main St", "price": 250000},
        ]
    }
