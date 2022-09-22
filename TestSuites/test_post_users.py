import pytest
import requests
import json
import random
import logging

LOGGER = logging.getLogger(__name__)


def test_post_users_validId_p0(api_v1_users):
    url = api_v1_users

    Id = 5
    UserName = "User 5"
    Password = "Password5"


    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    #actualResult = [value for elem in jsonResp
    #                  for value in elem.values()]
    #assert Id in actualResult
    #assert UserName in actualResult
    #assert Password in actualResult
    #assert jsonResp[4]["id"] == Id, resp.text
    #assert jsonResp[4]["userName"] == UserName, resp.text
    #assert jsonResp[4]["password"] == Password, resp.text
    # for i in range(len(jsonResp)):
        # assert jsonResp[i]["id"] == Id, resp.text
        # assert jsonResp[i]["userName"] == UserName, resp.text
        # assert jsonResp[i]["password"] ==Password, resp.text


def test_post_users_inValidUser_p1(api_v1_users):
    randomNum = random.randint(9000000, 9999999)
    url = api_v1_users

    Id = randomNum
    UserName = "UserInvalid"
    Password = "PasswordInvalid"

    data = {
        "id": Id ,
        "userName": UserName,
        "password": Password
    }
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    actualResult = [value for elem in jsonResp
                    for value in elem.values()]
    assert Id != actualResult
    assert UserName != actualResult
    assert Password != actualResult


def test_post_users_userNameNullalble_p2(api_v1_users):
    randomNum = random.randint(1, 10)
    url = api_v1_users

    Id = randomNum
    UserName = ""
    UserNameResp = "User 1"
    Password = "PasssWord"

    data = {
        "id": Id ,
        "userName": UserName,
        "password": Password
    }
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp[0]["userName"] == UserNameResp, resp.text


def test_post_users_passwordNullalble_p2(api_v1_users):
    randomNum = random.randint(1, 10)
    url = api_v1_users

    Id = randomNum
    UserName = "User 2"
    Password = ""
    PasswordResp = "Password2"

    data = {
        "id": Id ,
        "userName": UserName,
        "password": Password
    }
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp[1]["password"] == PasswordResp, resp.text


def test_post_users_idAsString_p2(api_v1_users):
    url = api_v1_users

    Id = "6"
    UserName = "User 5"
    Password = "Password5"

    data = {
        "id": Id
    }
    resp = requests.post(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    actualResult = [value for elem in jsonResp
                      for value in elem.values()]
    assert Id not in actualResult
