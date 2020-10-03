import argparse
import random


parser = argparse.ArgumentParser()
parser.add_argument('--size', help='Name to print', type=int, required=True)
parser.add_argument('--start', help='Last Name to print', type=int, required=True)
parser.add_argument('--end', help='Age to print', type=int, required=True)
parser.add_argument('--print', help='Print full name', action='store_true')
parser.add_argument('--numbers',  help='Options', nargs='+')
args = parser.parse_args()


numbers = []
for index in range(args.size):
    numbers.append(random.randint(args.start, args.end))
numbers.extend(args.numbers)
if args.print:
    print(numbers)


