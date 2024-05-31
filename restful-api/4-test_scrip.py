import requests

def test_home():
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
    assert response.text == "Welcome to the Flask API!"
    print("Test the home route of the API.: OK")

def test_data_no_users():
    response = requests.get('http://127.0.0.1:5000/data')
    assert response.status_code == 200
    assert response.json() == []
    print("Test the data route of the API when no users are added.: OK")

def test_add_user():
    new_user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    response = requests.post('http://127.0.0.1:5000/add_user', json=new_user)
    assert response.status_code == 200
    assert response.json() == {
        "message": "User added", 
        "user": new_user
    }
    print("Test adding a user to the API.: OK")

def test_data_after_adding_user():
    response = requests.get('http://127.0.0.1:5000/data')
    assert response.status_code == 200
    assert "john" in response.json()
    print("Test the data route of the API after adding a user.: OK")

def test_get_user():
    response = requests.get('http://127.0.0.1:5000/users/john')
    assert response.status_code == 200
    assert response.json() == {
        "username": "john", 
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print("Test getting a user from the API.: OK")

def test_get_user_not_exist():
    response = requests.get('http://127.0.0.1:5000/users/doesnotexist')
    assert response.status_code == 404
    assert response.json() == {"error": "User not found"}
    print("Test getting a user that does not exist.: OK")

def test_status():
    response = requests.get('http://127.0.0.1:5000/status')
    assert response.status_code == 200
    assert response.text == "OK"
    print("Test the status route of the API.: OK")

def test_add_user_no_username():
    new_user = {"name": "Alice", "age": 25, "city": "San Francisco"}
    response = requests.post('http://127.0.0.1:5000/add_user', json=new_user)
    assert response.status_code == 400
    assert response.json() == {"error": "Username is required"}
    print("Test adding a user without a username.: OK")

def test_add_user_duplicate():
    new_user = {"username": "john", "name": "John", "age": 30, "city": "New York"}
    response = requests.post('http://127.0.0.1:5000/add_user', json=new_user)
    assert response.status_code == 400
    assert response.json() == {"error": "User already exists"}
    print("Test adding a user with a duplicate username.: OK")

if __name__ == "__main__":
    test_home()
    test_data_no_users()
    test_add_user()
    test_data_after_adding_user()
    test_get_user()
    test_get_user_not_exist()
    test_status()
    test_add_user_no_username()
    test_add_user_duplicate()
