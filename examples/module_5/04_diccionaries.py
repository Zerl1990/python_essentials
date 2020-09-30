fmt_codes = {
    'header': '\033[95m',
    'blue': '\033[94m',
    'green': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'end': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

green = fmt_codes['green']
print(f'{green} Green color code')

yellow = fmt_codes.get('yellow', 'my_default_value')

# noinspection PyDictCreation
movie_duration = {'movie1': 120, 'movie2': 34, 'movie3': 30}

tmp = movie_duration.pop('movie1')
tmp = movie_duration.pop('movie1', 25)




