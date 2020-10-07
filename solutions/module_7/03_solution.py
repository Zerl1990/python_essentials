my_str = 'AABAAB'


def remove_adj_duplicates(msg):
    prev = None
    result = ''
    for char in msg:
        if char != prev:
            result += char
            prev = char
    return result


print(f'Original: {my_str}')
print(f'Result: {remove_adj_duplicates(my_str)}')