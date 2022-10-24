#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plotter python3 ../plotter.py
assert_no_stdout
assert_exit_code 0