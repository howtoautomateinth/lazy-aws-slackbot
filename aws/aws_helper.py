import requests

def get_instance_list():
    response = requests.get('API GATEWAY URL HERE')
    return response.json()