#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    d1 = res.json()

    row = []
    res2 = get('https://jsonplaceholder.typicode.com/users')
    d2 = res2.json()

    for i in d2:
        if i['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    row = []

    for i in d1:

        newDict = {}

        if i['userId'] == int(argv[1]):
            newDict['username'] = u_name
            newDict['task'] = i['title']
            newDict['completed'] = i['completed']
            row.append(newDict)

    fDict = {}
    fDict[id_no] = row
    json_obj = json.dumps(fDict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
