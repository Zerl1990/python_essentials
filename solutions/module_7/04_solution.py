my_msg = 'SOEMOSSOSEEE'



def detect_missing_chars(msg):
    diff = 0
    for index in range(0, len(msg), 3):
        if msg[index] != 'S':
            diff += 1
        if msg[index+1] != 'O':
            diff += 1
        if msg[index+2] != 'S':
            diff += 1
    return diff


print(f'Original: {my_msg}')
print(f'Missing: {detect_missing_chars(my_msg)}')
