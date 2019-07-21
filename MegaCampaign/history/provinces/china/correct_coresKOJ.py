import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('add_core=CXI', ''))
    sys.stdout.write(line.replace('add_core=X10', ''))
    sys.stdout.write(line.replace('add_core=CDL', ''))
    sys.stdout.write(line.replace('add_core=SHU', ''))
    sys.stdout.write(line.replace('add_core=CWU', ''))
    sys.stdout.write(line.replace('add_core=CHC', ''))
    sys.stdout.write(line.replace('add_core=ZHO', ''))
    sys.stdout.write(line.replace('add_core=MIN', ''))