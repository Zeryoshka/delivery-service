from pytest import fixture

from app.__main__ import create_app
from app.config import Config

@fixture()
async def test_client(aiohttp_client, mocker):
    mocker.patch('sys.argv', [])
    config = Config()
    app = create_app(config)
    return await aiohttp_client(app)
