from app import app

def test_home():
    client = app.test_client()
    assert client.get("/").status_code == 200

def test_login():
    client = app.test_client()
    res = client.post("/login", json={"username": "admin", "password": "admin"})
    assert res.status_code == 200

def test_add_client():
    client = app.test_client()
    res = client.post("/clients", json={"name": "John", "age": 25})
    assert res.status_code == 201

def test_add_workout():
    client = app.test_client()
    res = client.post("/workouts", json={"client_name": "John", "workout_type": "Cardio"})
    assert res.status_code == 201
