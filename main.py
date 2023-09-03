import requests

base_url = "https://petstore.swagger.io/v2"

# GET запрос
def get_request(path):
    url = base_url + path
    response = requests.get(url)
    return response.json()

# POST запрос
def post_request(path, data):
    url = base_url + path
    response = requests.post(url, json=data)
    return response.json()

# DELETE запрос
def delete_request(path):
    url = base_url + path
    response = requests.delete(url)
    return response.json()

# PUT запрос
def put_request(path, data):
    url = base_url + path
    response = requests.put(url, json=data)
    return response.json()

# Пример использования

# GET запрос на получение информации о питомце с id=1
pet_info = get_request("/pet/1")
print("GET response:", pet_info)

# POST запрос на создание нового питомца
new_pet_data = {
    "name": "Fluffy",
    "category": {
        "id": 1,
        "name": "Cats"
    },
    "status": "available"
}
created_pet_info = post_request("/pet", new_pet_data)
print("POST response:", created_pet_info)

# PUT запрос на обновление информации о питомце с id=1
updated_pet_data = {
    "id": 1,
    "name": "Fluffy",
    "category": {
        "id": 1,
        "name": "Cats"
    },
    "status": "pending"
}
updated_pet_info = put_request("/pet", updated_pet_data)
print("PUT response:", updated_pet_info)

# DELETE запрос на удаление питомца с id=1
deleted_pet_info = delete_request("/pet/1")
print("DELETE response:", deleted_pet_info)
