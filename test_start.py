from test_api import Store, Pet, User

store_api = Store()
pet_api = Pet()
user_api = User()


def test_01_store_API():
    store_api.get()
    store_api.post()
    store_api.get_order_id()
    store_api.delete_order_id()


def test_02_pet_API():
    pet_api.post_pet()
    pet_api.get_pet_by_status()
    pet_api.put_pet()
    pet_api.delete_pet()


def test_03_user_API():
    user_api.post_user()
    user_api.get_user()
    user_api.put_user()
    user_api.delete_user()
