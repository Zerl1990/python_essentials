import requests


def get_data_set():
    response = requests.get('http://api.worldbank.org/V2/country?incomeLevel=LIC&format=json')
    return response.json()


data_set = get_data_set()
print(data_set)
