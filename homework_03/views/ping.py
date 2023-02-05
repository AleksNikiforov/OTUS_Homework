import json
from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/ping", tags=["Ping"])


@router.get("")
def get_ping():
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
        status_code=200,
    )