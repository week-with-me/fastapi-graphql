import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    test: str


schema = strawberry.Schema(Query)
router = GraphQLRouter(schema=schema)
