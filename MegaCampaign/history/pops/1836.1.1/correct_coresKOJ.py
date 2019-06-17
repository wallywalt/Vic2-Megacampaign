import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('japanese', 'nihonjin'))
