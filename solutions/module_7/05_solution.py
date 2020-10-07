def get_unicode_total(msg):
    return sum(ord(char) for char in msg)


my_str_1 = 'ABC'
my_str_2 = 'CBE'

print(f'String 1: {my_str_1}')
print(f'String 1: {my_str_2}')
print(f'Unicode Diff: {get_unicode_total(my_str_1) - get_unicode_total(my_str_2)}')
