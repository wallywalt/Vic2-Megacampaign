import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('flintlock_rifles = 1\nflintlock_rifles = 1', 'flintlock_rifles = 1'))
