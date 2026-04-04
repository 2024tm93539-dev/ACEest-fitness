from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "aceest.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, role TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY AUTOINCREMENT, client_name TEXT, workout_type TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS metrics (id INTEGER PRIMARY KEY AUTOINCREMENT, client_name TEXT, weight REAL)")

    cur.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin','Admin')")

    conn.commit()
    conn.close()

init_db()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (data.get("username"), data.get("password")))
    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO clients (name, age) VALUES (?,?)", (data.get("name"), data.get("age")))
    conn.commit()
    conn.close()

    return jsonify({"message": "Client added"}), 201

@app.route("/clients", methods=["GET"])
def get_clients():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients")
    rows = cur.fetchall()
    conn.close()

    return jsonify(rows)

@app.route("/workouts", methods=["POST"])
def add_workout():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO workouts (client_name, workout_type) VALUES (?,?)",
                (data.get("client_name"), data.get("workout_type")))
    conn.commit()
    conn.close()

    return jsonify({"message": "Workout added"}), 201

@app.route("/metrics", methods=["POST"])
def add_metrics():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO metrics (client_name, weight) VALUES (?,?)",
                (data.get("client_name"), data.get("weight")))
    conn.commit()
    conn.close()

    return jsonify({"message": "Metrics added"}), 201

@app.route("/")
def home():
    return jsonify({"message": "ACEest Fitness API running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
