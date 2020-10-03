import requests

PROXIES = {
    "http": "http://www-proxy-adcq7-new.us.oracle.com:80",
    "https": "https://www-proxy-adcq7-new.us.oracle.com:80"
}


def get_data_set():
    response = requests.get('http://api.worldbank.org/V2/country?incomeLevel=LIC&format=json', proxies=PROXIES)
    return response.json()


data_set = get_data_set()
print(data_set)
