import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.replace('ruling_party', '#New Reforms\nconscription = two_year_draft\ndebt_law = serfdom\npenal_system = capital_punishment\nchild_labor = child_labor_legal\ncitizens_rights = primary_culture_only\nborder_policy = open_borders\ncentralization = unitary\ncolonial_policy = no_colonies\n\nruling_party'))
