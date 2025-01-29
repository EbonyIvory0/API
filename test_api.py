import requests
import json
import urllib3
URL = 'https://petstore.swagger.io/v2/store/'
PET_URL = "https://petstore.swagger.io/v2/pet"
USER_URL = "https://petstore.swagger.io/v2/user/"
headers = 'accept: application/json'
store_example = {
    "id": 4,
    "petId": 4,
    "quantity": 228,
    "shipDate": "2025-01-29T10:54:29.586Z",
    "status": "placed",
    "complete": True
}

pet_example = {
    "id": 1337,
    "category": {
    "id": 13,    
    "name": "megalodon"
},
    "name": "клык",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
    "id": 228,
    "name": "sweaty"
        }
    ],
    "status": "sold"
}

pet_put_example = {
    "id": 1337,
    "category": {
        "id": 13,    
        "name": "Альтрон11"
    },
    "name": "Альтрон11",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 228,
        "name": "sweaty"
        }
    ],
    "status": "sold"
    }
user_body = [
{
    "id": 23,
    "username": "AXE",
    "firstName": "Aleksandr",
    "lastName": "Xill",
    "email": "cullingblade@mail.ru",
    "password": "ihateignite",
    "phone": "+7-928-275-32-50",
    "userStatus": 1
}
]

put_user_body = [
{
    "id": 14,
    "username": "Magnus",
    "firstName": "Aleksandr",
    "lastName": "Xill",
    "email": "cullingblade@mail.ru",
    "password": "ihateignite",
    "phone": "+7-928-275-32-50",
    "userStatus": 2
}
]

class store:
    def GET():
            response = requests.get(URL + "inventory")
            assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
            response_json = response.json()# Преобразуем ответ в JSON
            assert response_json.get("нет") == 7, ">>>> ['нет']ERROR <<<<"# Проверяем, что в ответе есть ключ 'нет' и его значение равно 7
            print(response_json)
    def POST():
            response = requests.post(URL + "order", json=store_example)
            assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
            response_json = response.json()# Преобразуем ответ в JSON
            assert response_json.get("quantity") == 228, ">>>> ERROR <<<"# Проверяем, что в ответе есть ключ 'quantity' и его значение равно 228
            print(response_json)
    def GET_ORDER_ID():
            response = requests.get(URL + "order/4")# ID 1 to 10
            assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
            response_json = response.json() # Преобразуем ответ в JSON
            assert response_json.get("id") == 4, ">>>> ERROR <<<" # Проверяем, что в ответе есть ключ 'id' и его значение равно 4
            print(response_json)
    def DELETE_ORDER_ID():
            response = requests.delete(URL + "order/4")
            assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
            response_json = response.json()
            assert response_json.get("message") == "4", ">>>> DELETE ERROR <<<<"
            print(response_json)


class pet:
    def POST_pet():
        response = requests.post(PET_URL, json=pet_example)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("id") == 1337, ">>>> ID ERROR <<<<"
        print(response_json)
    def GET_pet_by_STATUS():
        response = requests.get(PET_URL + "/findByStatus?status=sold")
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        found = any(pet.get("id") == 1337 for pet in response_json)
        assert found, ">>>> Create pet not founded by ID <<<<"      # Проверяем, что хотя бы один объект в списке имеет id равный 1337      
    def PUT_pet():
        response = requests.put(PET_URL, json=pet_put_example)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("name") == "Альтрон11", ">>>> PUT ERROR <<<<"


    def DELETE_pet():
        response = requests.delete(PET_URL + "/1337")
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"

class user:
    def POST_user():
        response = requests.post(USER_URL + "createWithList", json=user_body)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("message") == "ok", ">>>> Create User ERROR <<<<"

    def GET_user():
        response = requests.get(USER_URL + "AXE")
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("username") == "AXE", ">>>> GET ERROR <<<<"

    def PUT_user():
        response = requests.put(USER_URL + "AXE", json=put_user_body)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("username") == "Magnus", ">>>> PUT ERROR <<<<"

    def DELETE_user():
        response = requests.delete(USER_URL + "Magnus")
        response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("message") == "Magnus", ">>>> DELETE ERROR <<<<"      