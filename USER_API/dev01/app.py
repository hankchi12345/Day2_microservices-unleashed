import os
import requests

API_HOST = os.getenv("USER_API_HOST", "localhost")
API_PORT = os.getenv("USER_API_PORT", "7000")

def find_user(user_id):
    res = requests.get(f"http://{API_HOST}:{API_PORT}/users/{user_id}")
    print(res.json())

def add_user(user_id, name):
    res = requests.post(f"http://{API_HOST}:{API_PORT}/users/", json={"id": user_id, "name": name})
    print(res.json())

if __name__ == "__main__":
    add_user(1, "Alice")
    find_user(1)
