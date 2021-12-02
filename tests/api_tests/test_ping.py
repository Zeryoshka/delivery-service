from http import HTTPStatus

async def test_ping(test_client):
    resp = await test_client.get('/ping')
    assert resp.status == HTTPStatus.OK