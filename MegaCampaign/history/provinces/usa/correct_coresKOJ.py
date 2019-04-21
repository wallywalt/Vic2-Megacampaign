import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('controller=NEN', 'controller=NEN\nadd_core=ENG'))
