from http import HTTPStatus

async def test_ping(test_client):
    resp = await test_client.get('/ping')
    assert resp.status == HTTPStatus.OK


async def test_db_ping_ok(test_client, mocker):
    mocker.patch('app.db.DB.ping')
    resp = await test_client.get('/ping_db')
    assert resp.status == HTTPStatus.OK

async def test_db_ping_fail(test_client, mocker):

    async def ping(_):
        raise Exception()

    mocker.patch('app.db.DB.ping', ping)
    resp = await test_client.get('/ping_db')
    assert resp.status == HTTPStatus.INTERNAL_SERVER_ERROR
