import requests
import pytest
from assertpy import assert_that

from lesson_09_playwright.api_requests_09 import response
from tests.conftest import base_url

def test_single_user_not_found(base_url):
    response= requests.get(f'{base_url}users/23')
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.reason).is_equal_to("Not Found")

def test_successful_login(base_url):
    user={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response =requests.post(f"{base_url}login",json=user)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key('token')
