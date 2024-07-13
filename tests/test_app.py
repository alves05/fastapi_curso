from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_curso.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo'}  # Asset
