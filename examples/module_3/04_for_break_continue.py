
for num in range(1, 11):
    tmp = num % 2
    if tmp == 0:
        print(f'We got a even number {num}, break!!!')
        break
    print(f'Number: {num}')


for num in range(1, 11):
    if num % 2 == 0:
        print(f'Do not multiple even numbers {num}, contiue!!!')
        continue
    print(f'result: {num*num}')
