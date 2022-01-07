import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient


class TestQNARoutes:
    @pytest.mark.asyncio
    async def test_rest_async(
        self,
        app: FastAPI,
        client: AsyncClient
    ) -> None:
        response = await client.post(
            url  = app.url_path_for('qna:create-qna'),
            json = {}
        )
        assert response.status_code != status.HTTP_404_NOT_FOUND


class TestQNACreate:
    
    pass