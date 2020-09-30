movie_duration = {'movie1': 120, 'movie2': 34, 'movie3': 30}

if 'movie1' in movie_duration:
    print('The movie exists!')

keys = movie_duration.keys()
print(type(keys))
for key in movie_duration.keys():
    print(key)


values = movie_duration.values()
print(type(values))
for value in movie_duration.values():
    print(value)

print(type(movie_duration.items()))
for key, value in movie_duration.items():
    print(f'[{key}] = {value}')

