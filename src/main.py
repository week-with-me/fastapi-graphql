from typing import Set
import uvicorn
from fastapi import FastAPI
from src.api import router
from src.core import get_settings


app = FastAPI(title = get_settings().PROJECT_TITLE)

app.include_router(
    router = router,
    prefix = get_settings().COMMON_API
)


if __name__ == '__main__':
    uvicorn.run('src.main:app', host='0.0.0.0', port=8000, reload=True)