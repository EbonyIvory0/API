
import requests
from test_api import store, pet

setup = store
setup2 = pet

def test_01():
    setup.GET()
    setup.POST()
    setup.GET_ORDER_ID()
    setup.DELETE_ORDER_ID()

def test_02():
    setup2.POST_pet()
    setup2.GET_pet_by_STATUS()
    setup2.PUT_pet()
    setup2.DELETE_pet()
    
