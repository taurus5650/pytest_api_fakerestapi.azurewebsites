import pytest
import requests
import json
import random
import logging

LOGGER = logging.getLogger(__name__)


def test_post_users_validId_p0(api_v1_users):
    url = api_v1_users

    Id = 5
    UserName = "UserTest"
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_userNameNullalble_p2(api_v1_users):
    randomNum = random.randint(1, 10)
    url = api_v1_users

    Id = randomNum
    UserName = None
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_passwordNullalble_p2(api_v1_users):
    randomNum = random.randint(1, 10)
    url = api_v1_users

    Id = randomNum
    UserName = "UserTest"
    Password = None

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_idAsStringWithNum_p2(api_v1_users):
    url = api_v1_users

    IdString = "78"
    Id = 78
    UserName = "UserTest"
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": IdString,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_idAsStringWithWords_p3(api_v1_users):
    url = api_v1_users

    Id = "string"
    UserName = "UserTest"
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 400
    assert jsonResp["errors"]["$.id"] == ['The JSON value could not be converted to System.Int32. Path: $.id | LineNumber: 0 | BytePositionInLine: 15.']


def test_post_users_userNameWithSymbol_p1(api_v1_users):
    url = api_v1_users

    Id = 86
    UserName = "User (Test) Hi2 %"
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_passwordWithSymbol_p1(api_v1_users):
    url = api_v1_users

    Id = 1099
    UserName = "UserTest"
    Password = "Pass 9(word) ^&*"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text


def test_post_users_largeUserId_p3(api_v1_users):
    randomNum = random.randint(900000000, 999999999)
    url = api_v1_users

    Id = randomNum
    UserName = "UserTest"
    Password = "PasswordTest"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id,
        "userName": UserName,
        "password": Password
    }

    resp = requests.request("POST", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + str(data))
    LOGGER.info("Resp : \n" + str(jsonResp))

    assert resp.status_code == 200
    assert jsonResp["id"] == Id, resp.text
    assert jsonResp["userName"] == UserName, resp.text
    assert jsonResp["password"] == Password, resp.text
