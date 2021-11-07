from src.core import get_settings
from src.api import graphql, rest
from fastapi import APIRouter


router = APIRouter()

router.include_router(
    router = graphql.router,
    prefix = get_settings().GRAPHQL_API,
    tags   = ['GraphQL']
)
