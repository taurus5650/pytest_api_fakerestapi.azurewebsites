import pytest
import requests
import json
import random
import logging

LOGGER = logging.getLogger(__name__)


def test_post_users_validId(api_v1_users):
    url = api_v1_users

    Id = 5
    UserName = "User 5"
    Password = "Password5"

    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp[4]["id"] == Id, resp.text
    assert jsonResp[4]["userName"] == UserName, resp.text
    assert jsonResp[4]["password"] == Password, resp.text
