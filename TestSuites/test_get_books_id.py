import pytest
import requests
import json
import random


def test_get_books_url_validId(api_v1_books):
    url = api_v1_books + "/35"
    data  = {}
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 200
    assert jsonResp["id"] == 35, resp.text
    assert jsonResp["title"] == "Book 35"
    assert jsonResp["pageCount"] == 3500


def test_get_books_url_notFound(api_v1_books):
    randomNum =  random.randint (9000000,9999999)
    url = api_v1_books + "/" + str(randomNum)
    data  = {}
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 404
    assert jsonResp["title"] == "Not Found", resp.text


def test_get_books_url_invalidId(api_v1_books):
    url = api_v1_books + "/9999999999"
    data  = {}
    resp = requests.get(url, data = data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '9999999999' is not valid."], resp.text


def test_get_books_url_string(api_v1_books):
    url = api_v1_books + "/string"
    data = {}
    resp = requests.get (url, data = data)
    jsonResp = json.loads(resp.text)
    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value 'string' is not valid."], resp.text


def test_get_books_url_withHash(api_v1_books):
    url = api_v1_books + "/#"
    data = {}
    resp = requests.get (url, data = data)
    jsonResp = json.loads(resp.text)
    assert resp.status_code == 200
    assert jsonResp[0]["id"] == 1, resp.text
    assert jsonResp[1]["id"] == 2, resp.text
    assert jsonResp[2]["id"] == 3, resp.text


def test_get_books_url_withSymbol(api_v1_books):
    url = api_v1_books + "/@!/"
    data = {}
    resp = requests.get (url, data = data)
    jsonResp = json.loads(resp.text)
    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '@!' is not valid."], resp.text
