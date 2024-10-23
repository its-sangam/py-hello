from numpy.f2py.auxfuncs import throw_error
from requests import get, post
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the base URL from the environment variables
BASE_URL = os.getenv('BASE_URL')
POST_URL = os.getenv('POST_URL')

# Make the API request using the base URL

def get_branch_list():
    try:
        req = get(f"{BASE_URL}/branchlist")
        if req.status_code == 200:
            info = req.json()
            branches = np.array(info['data'])
            print(f"Branches: {branches}")
        else:
            raise Exception(f"Error: Received status code {req.status_code}")

    except Exception as e:
        print(f"{e}")

def post_req_example():
    try:
        req = post(f"{POST_URL}/auth/login", headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, json={
            "email":"customer@gmail.com",
            "password":"password"
        })

        if req.status_code == 200:
            res = req.json()
            data = res['data']
            user = data['user']
            print(f"Successfully logged in with user {user['first_name']}  {user['last_name']}")
        else:
            raise Exception(f"Error: Received status code {req.status_code} with message {req.text}")
    except Exception as e:
        print(f"{e}")


# get_branch_list()
post_req_example()