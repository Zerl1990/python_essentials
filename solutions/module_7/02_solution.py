

def encrypt(n, message):
    result = ''
    for char in message:
        base_ord = ord('A') if char.isupper() else ord('a')
        if char.isalpha():
            shift_char = ord(char) + n
            shift_char = (shift_char - base_ord) % 26
            result += chr(base_ord + shift_char)
        else:
            result += char
    return result


def decrypt(n, message):
    result = ''
    for char in message:
        base_ord = ord('A') if char.isupper() else ord('a')
        if char.isalpha():
            shift_char = ord(char) - n
            shift_char = (shift_char - base_ord) % 26
            result += chr(base_ord + shift_char)
        else:
            result += char
    return result


MSG = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
N = 3
print(f'Original: {MSG}')
encrypted = encrypt(N, MSG)
print(f'Encrypted: {encrypted}')
decrypted = decrypt(N, encrypted)
print(f'Decrypted: {decrypted}')
