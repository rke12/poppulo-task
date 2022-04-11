# suites/my_suites.py:
# Task: Write code to create, read, update and delete an Employee of the Employee API.

from email import message
import json
import re
from tabnanny import check
from urllib import response
from venv import create
from wsgiref import headers
import requests
import urllib.request as request
# from urllib import request, response
import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *

headers={
    'Content-Type':'application/json',
    "User-Agent": "XY"
}

@lcc.test()
# Simple get request to start
def test_get():
    url = "http://dummy.restapiexample.com/api/v1/employee/1"
    response = requests.get(url=url, headers=headers)
    check_that("response code", response.status_code, equal_to(200))

@lcc.test()
# Post request to create new employee
def create_employee():
    url = "http://dummy.restapiexample.com/api/v1/create"
    response = requests.post(url=url, headers=headers,
    json={
        "name": "Johnathon Doe",
        "salary": "67000",
        "age": "39"
        }
    )
    check_that("response code", response.status_code, equal_to(200))
    employee_ID = response.json()['data']['id']
    return employee_ID
    
@lcc.test()
# Get request to return the Employee just created
def return_employee():
   url = "http://dummy.restapiexample.com/api/v1/employee/{}".format(create_employee())
   response = requests.get(url=url, headers=headers)
   check_that("response code", response.status_code, equal_to(200))

@lcc.test()
def update_employee():
    url = "http://dummy.restapiexample.com/api/v1/update/{}".format(create_employee())
    response = requests.put(headers=headers, url=url, 
    json={
        "employee_name": "Test McTestface",
        "employee_salary": 3120800,
        "employee_age": 6,
        "profile_image": ""
    })
    if response.status_code != 200:
        print(response.json()['message'])
    check_that("response code", response.status_code, equal_to(200))

@lcc.test()
def delete_employee():
    url = "http://dummy.restapiexample.com/public/api/v1/delete/{}".format(create_employee())
    response = requests.delete(headers=headers, url=url)
    check_that("response code", response.status_code, equal_to(200))