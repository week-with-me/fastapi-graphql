from fastapi import APIRouter

from src.api import graphql, rest
from src.core import get_settings

router = APIRouter()

router.include_router(
    router = graphql.router,
    prefix = get_settings().GRAPHQL_API,
    tags   = ['GraphQL']
)
router.include_router(
    router = rest.router,
    prefix = get_settings().REST_API
)