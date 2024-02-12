import sys

# This script processes a file of comma separated numbers, and 
# counts the number of time each number is found.

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

distribution = {}

for line in inputdata:

    for element in line.split(','):

        if int(element) in distribution:
            distribution[int(element)] += 1
        else:
            distribution[int(element)] = 1

        
keys = list(distribution.keys())
keys.sort()

for key in keys:    
    print(f"{key},{distribution[key]}")

