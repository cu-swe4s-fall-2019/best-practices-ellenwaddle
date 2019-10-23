# best-practices
##Best practices includes style.py, a file that defines functions one through four as a strings 'one' through 'four' (respectively). It also creates several functions for definitng complex numbers or sums of four numerical values. This script was created to practice proper style guides (See  ​https://pycodestyle.readthedocs.io​ for more detail).

##get_column_stats.py is a file that can take an input file (requires an str file of numerical values) and determines the number of columns within the file. It also can find the mean and sd of the values in the input file.



##how to use your project, with examples
##example.txt is an example input file. You should be able to add this file to your directory and run it:  
'''
`python get_column_stats.py --input_file example.txt column_number 1`
'''

# Setup

`conda update --yes conda
conda config --add channels bioconda
conda install pycodestyle
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
bash basics_test.sh

import sys
import pycodestyle
import os`
