import pytest
import requests
import json


def test_get_valid_id(supply_url):
    url = supply_url + "/35"
    data  = {}
    resp = requests.get(url, data=data)
    j = json.loads(resp.text)
    
    assert resp.status_code == 200
    assert j['id']==35, resp.text