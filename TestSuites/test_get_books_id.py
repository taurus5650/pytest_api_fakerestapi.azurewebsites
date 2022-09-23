import pytest
import requests
import json
import random
import logging

LOGGER = logging.getLogger(__name__)


def test_get_books_url_validId_p0(api_v1_books):
    url = api_v1_books + "/35"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 200
    assert jsonResp["id"] == 35, resp.text
    assert jsonResp["title"] == "Book 35", resp.text
    assert jsonResp["pageCount"] == 3500, resp.text


def test_get_books_url_notFound_p2(api_v1_books):
    randomNum = random.randint(9000000, 9999999)
    url = api_v1_books + "/" + str(randomNum)

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 404
    assert jsonResp["title"] == "Not Found", resp.text


def test_get_books_url_invalidId_p1(api_v1_books):
    url = api_v1_books + "/9999999999"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '9999999999' is not valid."], resp.text


def test_get_books_url_withoutId_requestId_p3(api_v1_books):
    url = api_v1_books

    Id = 15

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {
        "id": Id
    }

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 200
    assert len(jsonResp) > 1


def test_get_books_url_string_p2(api_v1_books):
    url = api_v1_books + "/string"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value 'string' is not valid."], resp.text


def test_get_books_url_withHash_p2(api_v1_books):
    url = api_v1_books + "/#"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 200
    assert jsonResp[0]["id"] == 1, resp.text
    assert jsonResp[1]["id"] == 2, resp.text
    assert jsonResp[2]["id"] == 3, resp.text


def test_get_books_url_withSymbol_p3(api_v1_books):
    url = api_v1_books + "/@!/"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '@!' is not valid."], resp.text


def test_get_books_url_withFloat_p3(api_v1_books):
    url = api_v1_books + "/4.6"

    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    data = {}

    resp = requests.request("GET", url,  headers=headers, data=json.dumps(data))
    jsonResp = json.loads(resp.text)
    LOGGER.info("Req : \n" + json.dumps(data, indent=2))
    LOGGER.info("Resp : \n" + json.dumps(jsonResp, indent=2))

    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '4.6' is not valid."], resp.text
