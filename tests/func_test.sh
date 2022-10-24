#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plotter python3 ../plotter.py --file_name '../iris.data'
assert_no_stdout
assert_exit_code 0

run test_plotter python3 ../plotter.py --file_name '../iris255.data'
assert_in_stdout 'Could not find'
assert_exit_code 1