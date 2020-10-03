import requests


def get_data_set():
    response = requests.get('http://api.worldbank.org/V2/country?incomeLevel=LIC&format=json')
    return response.json()


# Solution
data_set = get_data_set()
country_lst = data_set[1]
incomes = {}
regions = {}
for country in country_lst:
    income_level = country['incomeLevel']
    value = income_level['value']
    if value in incomes:
        incomes[value] = incomes[value] + 1
    else:
        incomes[value] = 1

    region = country['region']
    region_val = region['value']
    if region_val in regions:
        regions[region_val] = regions[region_val] + 1
    else:
        regions[region_val] = 1

print(incomes)
print(regions)
