import requests

def client():

    credentials  = {
        'username':'pemocham',
        'password':'pmc',

    }
    response = requests.post('http://127.0.0.1:8000/api/dj-rest-auth/login', data=credentials)

    print("Status Code:  ", response.status_code)

    response_data = response.ok
    print(response_data)


if __name__ == "__main__":
    client()