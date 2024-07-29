#!/usr/bin/python3

""" exports data in the CSV format """

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    d1 = res.json()

    row = []
    res2 = get('https://jsonplaceholder.typicode.com/users')
    d2 = res2.json()

    for i in d2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in d1:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                wr.writerow(row)
