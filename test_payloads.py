store_example = {
    "id": 4,
    "petId": 4,
    "quantity": 228,
    "shipDate": "2025-01-29T10:54:29.586Z",
    "status": "placed",
    "complete": True,
}

pet_example = {
    "id": 1337,
    "category": {"id": 13, "name": "megalodon"},
    "name": "клык",
    "photoUrls": ["string"],
    "tags": [{"id": 228, "name": "sweaty"}],
    "status": "sold",
}

pet_put_example = {
    "id": 1337,
    "category": {"id": 13, "name": "Альтрон11"},
    "name": "Альтрон11",
    "photoUrls": ["string"],
    "tags": [{"id": 228, "name": "sweaty"}],
    "status": "sold",
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
        "userStatus": 1,
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
        "userStatus": 2,
    }
]
