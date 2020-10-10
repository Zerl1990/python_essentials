def big_lst(limit):
    num = 0
    while num < limit:
        yield num
        num += 1


for n in big_lst(100000000):
    print(n)
