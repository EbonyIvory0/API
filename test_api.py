import requests
import test_payloads

URL = "https://petstore.swagger.io/v2/store/"
PET_URL = "https://petstore.swagger.io/v2/pet"
USER_URL = "https://petstore.swagger.io/v2/user/"
headers = "accept: application/json"


class Store:
    def get(self):
        response = requests.get(URL + "inventory", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()  # Преобразуем ответ в JSON
        assert (
            response_json.get("нет") == 7
        ), ">>>> ['нет']ERROR <<<<"  # Проверяем, что в ответе есть ключ 'нет' и его значение равно 7
        print(response_json)

    def post(self):
        response = requests.post(
            URL + "order", json=test_payloads.store_example, timeout=30
        )
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()  # Преобразуем ответ в JSON
        assert (
            response_json.get("quantity") == 228
        ), ">>>> ERROR <<<"  # Проверяем, что в ответе есть ключ 'quantity' и его значение равно 228
        print(response_json)

    def get_order_id(self):
        response = requests.get(URL + "order/4", timeout=10)  # ID 1 to 10
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()  # Преобразуем ответ в JSON
        assert (
            response_json.get("id") == 4
        ), ">>>> ERROR <<<"  # Проверяем, что в ответе есть ключ 'id' и его значение равно 4
        print(response_json)

    def delete_order_id(self):
        response = requests.delete(URL + "order/4", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("message") == "4", ">>>> DELETE ERROR <<<<"
        print(response_json)


class Pet:
    def post_pet(self):
        response = requests.post(PET_URL, json=test_payloads.pet_example, timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("id") == test_payloads.pet_example.get("id"), ">>>> ID ERROR <<<<"
        print(response_json)

    def get_pet_by_status(self):
        response = requests.get(PET_URL + "/findByStatus?status=sold", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        found = any(pet.get("id") == 1337 for pet in response_json) # Проверяем, что хотя бы один объект в списке имеет id равный 1337
        assert (
            found
        ), ">>>> Create pet not founded by ID <<<<"  

    def put_pet(self):
        response = requests.put(PET_URL, json=test_payloads.pet_put_example, timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("name") == "Альтрон11", ">>>> PUT ERROR <<<<"

    def delete_pet(self):
        response = requests.delete(PET_URL + "/1337", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"


class User:
    def post_user(self):
        response = requests.post(USER_URL + "createWithList", json=test_payloads.user_body, timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("message") == "ok", ">>>> Create User ERROR <<<<"

    def get_user(self):
        response = requests.get(USER_URL + "AXE", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("username") == "AXE", ">>>> GET ERROR <<<<"

    def put_user(self):
        response = requests.put(USER_URL + "AXE", json=test_payloads.put_user_body, timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("username") == "Magnus", ">>>> PUT ERROR <<<<"

    def delete_user(self):
        response = requests.delete(USER_URL + "Magnus", timeout=10)
        assert response.status_code == 200, ">>>> Status Code ERROR <<<<"
        response_json = response.json()
        assert response_json.get("message") == "Magnus", ">>>> DELETE ERROR <<<<"
