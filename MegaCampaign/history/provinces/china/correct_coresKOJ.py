import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('add_core=MGL', 'add_core=MGL\nadd_core=X10'))
