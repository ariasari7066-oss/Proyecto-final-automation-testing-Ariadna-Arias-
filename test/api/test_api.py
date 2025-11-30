import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# ==================================================================
# 1) GET POSTS
# ==================================================================
def test_get_posts():
    """Validar GET: obtener lista de posts"""
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Validar estructura del primer post
    post = data[0]
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post


# ==================================================================
# 2) POST - CREATE POST
# ==================================================================
def test_create_post():
    """Validar POST: creación de un recurso"""
    payload = {
        "title": "Post de prueba",
        "body": "Contenido generado desde test",
        "userId": 1
    }

    r = requests.post(f"{BASE_URL}/posts", json=payload)

    # JSONPlaceholder devuelve 201 siempre para creación simulada
    assert r.status_code == 201

    new_post = r.json()
    assert new_post["title"] == payload["title"]
    assert new_post["body"] == payload["body"]
    assert new_post["userId"] == payload["userId"]
    assert "id" in new_post  # ID generado


# ==================================================================
# 3) DELETE POST
# ==================================================================
def test_delete_post():
    """Validar DELETE: borrado simulado"""
    r = requests.delete(f"{BASE_URL}/posts/1")

    # JSONPlaceholder devuelve 200 y un body vacío
    assert r.status_code == 200

    body = r.json()
    assert body == {}  # Simula borrado


# ==================================================================
# 4) ENCADENAMIENTO (Crear → Obtener)
# ==================================================================
def test_create_then_get_post():
    """Flujo encadenado: crear un post y luego intentar obtenerlo"""

    # 1) Crear recurso
    payload = {
        "title": "Encadenado",
        "body": "Contenido encadenado",
        "userId": 99
    }

    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201

    created = r.json()
    created_id = created["id"]

    # 2) Obtener recurso creado
    r2 = requests.get(f"{BASE_URL}/posts/{created_id}")

    # JSONPlaceholder NO guarda estados,
    # así que puede devolver: 
    # ✔ 200 si el ID existe en rango 1–100
    # ✔ 404 si el ID generado está fuera del rango
    assert r2.status_code in (200, 404)

    # Validación condicional
    if r2.status_code == 200:
        post = r2.json()
        assert "id" in post
        assert "title" in post
    else:
        # 404 esperado para IDs fuera del rango → JSON vacío
        assert r2.json() == {}  #  respuesta vacía