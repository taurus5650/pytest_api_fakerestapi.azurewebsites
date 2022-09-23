import pytest
import logging

LOGGER = logging.getLogger(__name__)
fakerestApi = "https://fakerestapi.azurewebsites.net"


@pytest.fixture()
def api_v1_books ():
   api = "/api/v1/Books"
   LOGGER.info (fakerestApi + api + " Triggered")
   return fakerestApi + api


@pytest.fixture()
def api_v1_users ():
   api = "/api/v1/Users"
   LOGGER.info (fakerestApi + api + " Triggered")
   return fakerestApi + api

