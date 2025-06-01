from fastapi import FastAPI, HTTPException
import mysql.connector
import os

app = FastAPI()

def get_conn():
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        database=os.environ['DB_NAME']
    )

@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/")
def create_user(user: dict):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user['id'], user['name']))
    conn.commit()
    conn.close()
    return {"status": "created"}
