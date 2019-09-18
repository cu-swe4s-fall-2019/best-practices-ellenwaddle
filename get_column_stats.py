import sys
import math
import argparse

parser = argparse.ArgumentParser(description='supply file and colnum')

parser.add_argument('--file_name', type=str, help='your file',required=True)

parser.add_argument('--column_number', type=int, help='number of columns',
                    required=True)

args = parser.parse_args()
print(args.file_name, args.column_number)

f=open(file_name,'r')

#try:
#    f = open(file_name) #this needs to be fixed to be generic
#except FileNotFoundError:
#    print('Could not locate' + file_name)
#    sys.exit(1)
#except PermissionError:
#    print('Could not access' + file_name)
#    sys.exit(1)

V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[col_num])

mean = sum(V)/len(V)
return mean

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
return stdev

print('mean:', mean)
print('stdev:', stdev)
