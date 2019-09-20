import unittest
import get_column_stats
import sys
import so

#check code styling for all files
pycodestyle style.py
pycodestyle get_column_stats.py

test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run python get_column_stats.py --file_name example.txt --column_number 1
assert_exit_code 0


run python get_column_stats.py --file_name example.txt --column_number 1
assert_no_stderr
assert_in_stdout "mean: 10"
assert_in_stdout "stdev: 7.0710678118654755"

#testing w random integers
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run python get_column_stats.py --file_name data.txt --column_number 1
assert_no_stderr
assert_exit_code 0

run python get_column_stats.py --file_name example.txt --column_number 0
assert_exit_code 1

V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run python get_column_stats.py --file_name data.txt --column_number 5
assert_in_stdout "mean: 1.0"
assert_in_stdout "stdev: 0.0"
assert_no_stderr
assert_exit_code 0
