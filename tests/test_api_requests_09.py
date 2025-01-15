import pytest
import requests
from assertpy import assert_that

from tests.conftest import base_url


def test_get_requests(base_url):
   response= requests.get(f'{base_url}users/')
   assert response.status_code==200

def test_post_requests(base_url):
   #new_name is keeping the value to prevent failing because of mismatch names
   new_name = "Mali"
   new_user = {"name": new_name, "job": "QA"}
   response = requests.post(f'{base_url}users/', json=new_user)

   assert response.status_code==201
   assert 'id' in response.json()
   assert response.json()['name']==new_name

def test_delete_requests(base_url):
   response = requests.delete(f'{base_url}/users')

   assert response.status_code ==204
   #test if it returns with  an empty string
   assert response.text ==""

params=[(1,"george.bluth@reqres.in" ), (4,"eve.holt@reqres.in" )]
@pytest.mark.parametrize("user_id, email", params)
def test_get_with_params(user_id, email, base_url):
   response = requests.get(f'{base_url}/users{user_id}')

   assert response.status_code == 200
   # it's the same as the previous line
   assert_that(response.status_code).is_equal_to(200)

   assert response.json()['data']['id']==user_id
   #it's the same as the previous line
   assert_that(response.json()['data']).contains_entry({'id':user_id})

   assert response.json()['data']['email']==email


