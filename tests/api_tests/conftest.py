from pytest import fixture

from app.__main__ import create_app

@fixture()
async def test_client(aiohttp_client):
    app = create_app()
    return await aiohttp_client(app)
