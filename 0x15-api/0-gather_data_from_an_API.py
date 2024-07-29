#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    d1 = res.json()
    done = 0
    total = 0
    tasks = []
    res2 = get('https://jsonplaceholder.typicode.com/users')
    d2 = res2.json()

    for j in d2:
        if j.get('id') == int(argv[1]):
            employee = j.get('name')

    for j in d1:
        if j.get('userId') == int(argv[1]):
            total += 1

            if j.get('completed') is True:
                done += 1
                tasks.append(j.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, done,
                                                          total))

    for j in tasks:
        print("\t {}".format(j))
