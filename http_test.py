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
    sample = {"hobbies": "taking a bite out of crime"}
    url = "http://127.0.0.1:5000/users/14"
    #I've tried this in like 5 different configurations                                                                                "}
    resp = requests.put(url , json=sample)
    pprint(resp.json())


if __name__ == "__main__":
    # print("Scan request:")
    # scan()
    # print("Create request:")
    # create()
    test_update()