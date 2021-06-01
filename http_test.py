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
        "first_name": "Mike",
        "last_name": "Schmidtt",
        "hobbies": "things"
    }
    out = requests.post(url, json=test_data)
    pprint(out.json())


if __name__ == "__main__":
    print("Scan request:")
    scan()
    print("Create request:")
    create()