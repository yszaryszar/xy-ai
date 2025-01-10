# backend/tests/test_api/test_menus.py

import pytest
from fastapi.testclient import TestClient

from app.main import app  # 确保导入你的 FastAPI 实例

client = TestClient(app)


@pytest.fixture
def mock_get_menu(monkeypatch):
    def mock_return():
        return [
            {"id": 1, "name": "Menu 1"},
            {"id": 2, "name": "Menu 2"},
        ]

    monkeypatch.setattr("app.crud.menus.get_menu", mock_return)


def test_read_menu_success(mock_get_menu):
    response = client.get("/v1/menus/")
    # print(response.json())  # 添加此行以打印实际响应
    assert response.status_code == 200
    assert response.json() == {
        "code": 200,
        "message": "Get menus successfully",
        "data": [
            {"id": 1, "name": "Menu 1"},
            {"id": 2, "name": "Menu 2"},
        ],
    }


def test_read_menu_not_found(monkeypatch):
    def mock_return():
        return []

    monkeypatch.setattr("app.crud.menus.get_menu", mock_return)

    response = client.get("/v1/menus/")
    # print(response.json())  # 添加此行以打印实际响应
    assert response.status_code == 200
    assert response.json() == {
        "code": 200,
        "message": "Menus not found",
        "data": None,
    }
