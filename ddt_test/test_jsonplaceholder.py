import requests
import pytest


# Получение списка всех пользователей
def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0


# Получение списка постов для определенного пользователя
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0
    for post in posts:
        assert post["userId"] == user_id


# Получение списка комментариев для определенного поста
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0
    for comment in comments:
        assert comment["postId"] == post_id


# Получение списка альбомов для определенного пользователя
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_albums_by_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums?userId={user_id}")
    assert response.status_code == 200
    albums = response.json()
    assert len(albums) > 0
    for album in albums:
        assert album["userId"] == user_id


# Получение списка задач для определенного пользователя
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_todos_by_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0
    for todo in todos:
        assert todo["userId"] == user_id
