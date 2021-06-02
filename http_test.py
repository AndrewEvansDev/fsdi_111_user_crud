#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Helper file to test endpoints manually"""

import requests
from pprint import pprint


def scan():
    url = "http://127.0.0.1:5000/users"
    out = requests.get(url)
    pprint(out.json())


def create():
    url = "http://127.0.0.1:5000/users"
    test_data = {
        "first_name": "Rick",
        "last_name": "Jacks",
        "hobbies": "Selling pot"
    }
    out = requests.post(url, json=test_data)
    pprint(out.json())

def test_update():
    sample = ("hobbies","Golfing")                                                                                 "}
    resp = requests.put("http://127.0.0.1:5000/users/14", json=sample)
    pprint(resp.json())


if __name__ == "__main__":
    # print("Scan request:")
    # scan()
    # print("Create request:")
    # create()
    test_update()