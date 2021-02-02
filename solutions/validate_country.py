"""Validate covid metrics."""
import sys
import requests
import statistics
import matplotlib.pyplot as plt
import seaborn as sns


URL = 'https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST'


def download_covid_metrics() -> dict:
    """Download covid metrics."""
    resp = requests.get(URL)
    if resp.ok:
        return resp.json()
    else:
        raise RuntimeError(f'Cannot retrieve covid metrics: {resp.raw}')


def print_total_infected(data_set: dict, countries: list):
    """Search countries and print total infected

    :param data_set: List with information per each country
    :param countries: Country names to search for
    :return: None
    """
    for c_info in data_set:
        if c_info['country'] in countries:
            print(f"{c_info['country']} total infected: {c_info['infected']}")


def get_stats(data_set: dict, attribute) -> tuple:
    """Get statistics from covid infected metrics

    :param data_set: List with information per each country
    :param attribute: Attribute to get stats
    :return: Mean, Median, Standard Deviation
    """
    infected = [item[attribute] for item in data_set]
    return statistics.mean(infected), statistics.median(infected), statistics.stdev(infected)


def get_min_max_country(data_set: dict, attribute: str) -> dict:
    """Print country with max and min value

    :param data_set: List with information per each country
    :param attribute: Attribute to get stats
    :return: Country min, max info
    """
    max_name = None
    min_name = None
    max_count = 0
    min_count = sys.maxsize
    for c_info in data_set:
        if c_info[attribute] > max_count:
            max_count = c_info[attribute]
            max_name = c_info['country']
        if c_info[attribute] < min_count:
            min_count = c_info[attribute]
            min_name = c_info['country']
    return {'min_country': min_name, 'min_count': min_count, 'max_country': max_name, 'max_count': max_count}


metrics = download_covid_metrics()
print_total_infected(metrics, ['United States', 'China', 'France'])
mean, median, stdev = get_stats(metrics, 'infected')
print('Infected Stats:')
print(f'\tMean: {mean}')
print(f'\tMedian: {median}')
print(f'\tStandard Deviation: {stdev}')
min_max_info = get_min_max_country(metrics, 'infected')
print(f'Min Max info for infected: {min_max_info}')

# Extra plot infected
infected = [item['infected'] for item in metrics]
infected.sort()
plt.hist(infected, 20)
plt.show()
