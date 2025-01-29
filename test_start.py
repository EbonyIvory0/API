import pytest
import requests
from test_api import store, pet, user

store_api = store
pet_api = pet
user_api = user

def test_01_store_API():
    store_api.GET()
    store_api.POST()
    store_api.GET_ORDER_ID()
    store_api.DELETE_ORDER_ID()

def test_02_pet_API():
    pet_api.POST_pet()
    pet_api.GET_pet_by_STATUS()
    pet_api.PUT_pet()
    pet_api.DELETE_pet()

def test_03_user_API():
    user_api.POST_user()
    user_api.GET_user()
    user_api.PUT_user()
    user_api.DELETE_user()