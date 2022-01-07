from fastapi import APIRouter

from src.api.rest import qna

router = APIRouter()

router.include_router(
    router = qna.router,
    prefix = '/qna',
    tags   = ['QnA']
)