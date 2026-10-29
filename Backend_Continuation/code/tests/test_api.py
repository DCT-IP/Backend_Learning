from uuid import uuid4
import pytest


def make_user():
    suffix = uuid4().hex[:12]
    return {
        "FirstName": "Test",
        "LastName": "User",
        "Email": f"test_{suffix}@example.com",
        "Password": "TestPassword123!",
    }

def register_user(client, user):
    return client.post("/auth/register", json=user)

def login_user(client, user):
    return client.post(
        "/auth/login",
        data={
            "username": user["Email"],
            "password": user["Password"],
        },
    )

def get_auth_headers(client, user):
    response = login_user(client, user)
    assert response.status_code == 200, response.text
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_register_user(client):
    user = make_user()
    response = register_user(client, user)
    assert response.status_code == 201
    body = response.json()
    assert body["Email"] == user["Email"]
    assert "Password" not in body
    assert "PasswordHash" not in body


def test_register_duplicate_email(client):
    user = make_user()
    first_response = register_user(client, user)
    assert first_response.status_code == 201
    second_response = register_user(client, user)
    assert second_response.status_code == 409

def test_login_success(client):
    user = make_user()
    registration = register_user(client, user)
    assert registration.status_code == 201
    response = login_user(client, user)
    assert response.status_code == 200
    body = response.json()
    assert body["access_token"]
    assert body["token_type"].lower() == "bearer"

def test_login_wrong_password(client):
    user = make_user()
    registration = register_user(client, user)
    assert registration.status_code == 201
    response = client.post(
        "/auth/login",
        data={
            "username": user["Email"],
            "password": "WrongPassword123!",
        },
    )
    assert response.status_code == 401


def test_login_unknown_user(client):
    user = make_user()
    response = login_user(client, user)
    assert response.status_code == 401

def test_books_reject_missing_token(client):
    response = client.get("/books")
    assert response.status_code == 401

def test_books_reject_invalid_token(client):
    response = client.get(
        "/books",
        headers={"Authorization": "Bearer invalid.token.value"},
    )
    assert response.status_code == 401

def test_books_accept_valid_token(client):
    user = make_user()
    registration = register_user(client, user)
    assert registration.status_code == 201
    headers = get_auth_headers(client, user)
    response = client.get("/books", headers=headers)
    assert response.status_code == 200

def test_book_crud_lifecycle(client):
    user = make_user()
    registration = register_user(client, user)
    assert registration.status_code == 201
    headers = get_auth_headers(client, user)
    book = {
        "BookName": "Test Book",
        "Author": "Test Author",
        "Publisher": "Test Publisher",
        "Price": 499.00,
        "Quantity": 5,
    }
    create_response = client.post(
        "/books",
        json=book,
        headers=headers,
    )
    assert create_response.status_code == 201, create_response.text
    created = create_response.json()
    book_id = created["B_ID"]
    assert created["BookName"] == book["BookName"]
    assert created["Author"] == book["Author"]
    read_response = client.get(
        f"/books/{book_id}",
        headers=headers,
    )
    assert read_response.status_code == 200
    assert read_response.json()["B_ID"] == book_id
    list_response = client.get("/books", headers=headers)
    assert list_response.status_code == 200
    assert any(
        item["B_ID"] == book_id
        for item in list_response.json()
    )
    update_response = client.put(
        f"/books/{book_id}",
        json={"BookName": "Updated Test Book"},
        headers=headers,
    )
    assert update_response.status_code == 200, update_response.text
    assert update_response.json()["BookName"] == "Updated Test Book"
    delete_response = client.delete(
        f"/books/{book_id}",
        headers=headers,
    )
    assert delete_response.status_code in (200, 204)
    missing_response = client.get(
        f"/books/{book_id}",
        headers=headers,
    )
    assert missing_response.status_code == 404

def test_book_cache_invalidated_after_creation(client):
    user = make_user()
    registration = register_user(client, user)
    assert registration.status_code == 201
    headers = get_auth_headers(client, user)
    first_response = client.get("/books/", headers=headers)
    assert first_response.status_code == 200
    book = {
        "BookName": "Cache Test Book",
        "Author": "Cache Author",
        "Publisher": "Cache Publisher",
        "Price": 299.00,
        "Quantity": 3,
    }
    create_response = client.post(
        "/books/",
        json=book,
        headers=headers,
    )
    assert create_response.status_code == 201, create_response.text
    created_book_id = create_response.json()["B_ID"]
    second_response = client.get("/books/", headers=headers)
    assert second_response.status_code == 200
    books = second_response.json()
    assert any(
        item["B_ID"] == created_book_id
        for item in books
    )