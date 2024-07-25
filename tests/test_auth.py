from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        'auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_login_email_incorrect(client):
    response = client.post(
        'auth/token',
        data={'username': 'joao@email.com', 'password': 'pass123'},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_login_password_incorrect(client):
    client.post(
        '/users/',
        json={
            'username': 'joao',
            'email': 'joao@email.com',
            'password': 'pass123',
        },
    )

    response = client.post(
        'auth/token',
        data={'username': 'joao@email.com', 'password': 'pss123'}
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}