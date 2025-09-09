from app import app
import json

def test_hello_default():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["message"] == "Hello, World!"

def test_hello_with_name():
    client = app.test_client()
    resp = client.get("/?name=Tester")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["message"] == "Hello, Tester!"
