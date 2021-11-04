import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


async def test() -> str:
    return "Hello, GraphQL!"


@strawberry.type
class Query:
    test: str = strawberry.field(resolver=test)


schema = strawberry.Schema(Query)
graphql_router = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_router, prefix='/graphql')