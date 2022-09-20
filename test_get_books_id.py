import pytest
import requests
import json
import random


def test_get_books_validId(supply_url):
    url = supply_url + "/35"
    data  = {}
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 200
    assert jsonResp["id"] == 35, resp.text


def test_get_books_notFound(supply_url):
    randomNum =  random.randint (9000000,9999999)
    url = supply_url + "/" + str(randomNum)
    data  = {}
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 404
    assert jsonResp["title"] == "Not Found", resp.text


def test_get_books_invalidId(supply_url):
    url = supply_url + "/9999999999" 
    data  = {}
    resp = requests.get(url, data=data)
    jsonResp = json.loads(resp.text)
    
    assert resp.status_code == 400
    assert jsonResp["title"] == "One or more validation errors occurred.", resp.text
    assert jsonResp["errors"]["id"] == ["The value '9999999999' is not valid."], resp.text