#!/usr/bin/python3

""" exports data in the JSON format """

from requests import get
import json

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    d1 = res.json()

    row = []
    res2 = get('https://jsonplaceholder.typicode.com/users')
    d2 = res2.json()

    newDict = {}

    for j in d2:

        row = []
        for i in d1:

            newDict2 = {}

            if j['id'] == i['userId']:

                newDict2['username'] = j['username']
                newDict2['task'] = i['title']
                newDict2['completed'] = i['completed']
                row.append(newDict2)

        newDict[j['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(newDict)
        f.write(json_obj)
