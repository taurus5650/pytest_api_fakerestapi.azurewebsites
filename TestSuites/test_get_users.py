import pytest
import requests
import json
import random
import logging

LOGGER = logging.getLogger(__name__)


def test_get_users_validId_p0(api_v1_users):
    url = api_v1_users

    Id = 5
    UserName = "User 5"
    Password = "Password5"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    #LOGGER.info("Req : \n" + str(data))
    #LOGGER.info("Resp : \n" + str(jsonResp))
    #Pretty print, use json.dumps, indent
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 200
    # Fetch all keywords
    actualResult = [value for elem in jsonResp
                      for value in elem.values()]
    # When keyword - Username == User 5 in resp then pass
    assert Id in actualResult
    assert UserName in actualResult
    assert Password in actualResult
    # assert jsonResp[4]["id"] == Id, resp.text
    # assert jsonResp[4]["userName"] == UserName, resp.text
    # assert jsonResp[4]["password"] == Password, resp.text
    # for i in range(len(jsonResp)):
        # assert jsonResp[i]["id"] == Id, resp.text
        # assert jsonResp[i]["userName"] == UserName, resp.text
        # assert jsonResp[i]["password"] ==Password, resp.text
