import json
from unittest.mock import AsyncMock

import pytest
from bson import ObjectId
from fastapi import HTTPException

from app.handler.user_handler import UserHandler


def response_json(response):
    return json.loads(response.body.decode())


def make_service():
    service = AsyncMock()
    object_id = ObjectId("64f1b9f1b9f1b9f1b9f1b9f1")
    service.create_user.return_value = {"id": 1}
    service.get_user.return_value = {"_id": object_id, "id": 1, "name": "Alice"}
    service.update_user.return_value = {"id": 1, "name": "Alice Updated"}
    service.delete_user.return_value = {"deleted": True}
    service.get_all_users.return_value = [{"_id": object_id, "id": 1, "name": "Alice"}]
    service.get_user_by_email.return_value = {"id": 1, "email": "alice@example.com"}
    return service


def test_create_user_returns_created_response(run_async, user_schema):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.create_user(user_schema))

    service.create_user.assert_awaited_once_with(user_schema)
    assert response.status_code == 201
    assert response_json(response) == {"id": 1}


def test_get_user_returns_user_response(run_async):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.get_user(1))

    service.get_user.assert_awaited_once_with(1)
    assert response.status_code == 200
    assert response_json(response) == {
        "_id": "64f1b9f1b9f1b9f1b9f1b9f1",
        "id": 1,
        "name": "Alice",
    }


def test_get_user_raises_not_found_when_missing(run_async):
    service = make_service()
    service.get_user.return_value = None
    handler = UserHandler(service)

    with pytest.raises(HTTPException) as exc_info:
        run_async(handler.get_user(1))

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "User not found"


def test_update_user_returns_updated_response(run_async, user_schema):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.update_user(1, user_schema))

    service.update_user.assert_awaited_once_with(1, user_schema)
    assert response.status_code == 200
    assert response_json(response) == {"id": 1, "name": "Alice Updated"}


def test_update_user_raises_not_found_when_missing(run_async, user_schema):
    service = make_service()
    service.update_user.return_value = None
    handler = UserHandler(service)

    with pytest.raises(HTTPException) as exc_info:
        run_async(handler.update_user(1, user_schema))

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "User not found"


def test_delete_user_returns_deleted_response(run_async):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.delete_user(1))

    service.delete_user.assert_awaited_once_with(1)
    assert response.status_code == 200
    assert response_json(response) == {"deleted": True}


def test_delete_user_raises_not_found_when_missing(run_async):
    service = make_service()
    service.delete_user.return_value = None
    handler = UserHandler(service)

    with pytest.raises(HTTPException) as exc_info:
        run_async(handler.delete_user(1))

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "User not found"


def test_get_all_users_returns_users_response(run_async):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.get_all_users())

    service.get_all_users.assert_awaited_once_with()
    assert response.status_code == 200
    assert response_json(response) == [
        {"_id": "64f1b9f1b9f1b9f1b9f1b9f1", "id": 1, "name": "Alice"}
    ]


def test_get_user_by_email_returns_user_response(run_async):
    service = make_service()
    handler = UserHandler(service)

    response = run_async(handler.get_user_by_email("alice@example.com"))

    service.get_user_by_email.assert_awaited_once_with("alice@example.com")
    assert response.status_code == 200
    assert response_json(response) == {"id": 1, "email": "alice@example.com"}
