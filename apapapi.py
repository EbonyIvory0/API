import requests

PET_URL = "https://petstore.swagger.io/v2/pet"


payload = {
    "id": 0,
    "category": {"id": 0, "name": "string"},
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available",
}
class Pet:
    def post_pet():
        response = requests.post(PET_URL, json=payload, timeout=10)
        assert response.status_code == 200, "!<><><><><>!"
        response_json = response.json()
        assert response_json.get()