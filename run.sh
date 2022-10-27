#!/bin/bash

#set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if prior step failed

# Run plot_gtex.py
python plotter.py --file_name 'iris.data'

# test code style
pycodestyle plotter.py
pycodestyle data_processor.py
pycodestyle tests/unit_test.py

cd tests
python3 unit_test.py
bash func_test.sh
