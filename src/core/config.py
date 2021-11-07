from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    LEVEL: str = 'DEVELOP'
    PROJECT_TITLE: str = 'FastAPI with GraphQL and REST'
    GRAPHQL_API: str = '/graphql'
    REST_API: str = '/rest'
    COMMON_API: str = '/api'
    

class DevelopSettings(Settings):
    DB_URL: str

    class Config:
        env_file = 'src/core/develop.env'
     

class ProductSettings(Settings):
    DB_URL: str

    class Config:
        env_file = 'src/core/product.env'


@lru_cache
def get_settings(level='DEVELOP'):
    return DevelopSettings() if level is 'DEVELOP' else ProductSettings()