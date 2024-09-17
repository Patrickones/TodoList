from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_todo_list.app import app


def test_deve_retornar_ola_mundo_em_html():
    client = TestClient(app)
    response = client.get('/olamundo')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Asssert (afirmação)
    assert {'message': 'Olá Mundo'}, {'batata': 'frita'} in response.json()
