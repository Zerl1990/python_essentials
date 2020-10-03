import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Name to print', type=str, required=True)
parser.add_argument('--last-name', help='Last Name to print', type=str, required=False)
parser.add_argument('--age', help='Age to print', type=int, default=30)
parser.add_argument('--print', help='Print full name', action='store_true')
parser.add_argument('--opt',  help='Options', choices=['opt1', 'opt2', 'opt3'])
parser.add_argument('--list',  help='Options', nargs='+')
args = parser.parse_args()
print(args.name)
print(args.last_name)
print(args.name)
print(args.age)
print(args.print)
print(args.opt)


