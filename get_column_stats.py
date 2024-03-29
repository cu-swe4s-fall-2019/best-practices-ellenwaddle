import sys
import math
import argparse
"""
grab a column out of a specified file and returns mean and stdev of that column
"""

parser = argparse.ArgumentParser(description='supply file & colnum',
                                 prog='good way')

parser.add_argument('--file_name', type=str, help='your file', required=True)

parser.add_argument('--column_number', type=int, help='number of columns',
                    required=True)

args = parser.parse_args()
print(args.file_name, args.column_number)


if args.column_number < 0:
    print('Must have at least one column')
    sys.exit(1)

try:
    f = open(args.file_name, 'r')  # open file of interest
except FileNotFoundError:
    print('Could not locate' + file_name)
    sys.exit(1)
except PermissionError:
    print('Could not access' + file_name)
    sys.exit(1)


V = []

for l in f:
    try:
        A = [int(x) for x in l.split()]  # go through each line
        V.append(A[args.column_number-1])
    except ValueError:
        sys.exit(1)


def mean(V):
    """
    defines the mean fct
    """
    return sum(V)/len(V)


def stdev(V):
    """
    defines the mean fct
    """
    return math.sqrt(sum([(mean(V)-x)**2 for x in V]) / len(V))


print('mean:', mean(V))  # show output of mean to user
print('stdev:', stdev(V))  # show output of mean to user

if __name__ == 'main':
    unittest.main()
