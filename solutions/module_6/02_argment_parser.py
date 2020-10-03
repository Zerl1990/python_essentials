import argparse
import random


parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, required=True)
parser.add_argument('--start', type=int, required=True)
parser.add_argument('--end', type=int, required=True)
parser.add_argument('--print', action='store_true')
parser.add_argument('--numbers', nargs='+')
args = parser.parse_args()


numbers = []
for index in range(args.size):
    numbers.append(random.randint(args.start, args.end))
numbers.extend(args.numbers)

if args.print:
    print(numbers)


