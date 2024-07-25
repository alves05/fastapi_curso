from http import HTTPStatus

from jwt import decode

from fastapi_curso.security import Settings, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM]
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
