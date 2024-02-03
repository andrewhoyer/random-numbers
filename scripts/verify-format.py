import sys

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

all_lines_valid = True

for line in inputdata:
    if len(line.split(',')) != 10:
        all_lines_valid = False
        break

if all_lines_valid:
    print(f"✅ Data in {argv1} is valid")
else:
    print(f"🚨 Data in {argv1} is invalid")
