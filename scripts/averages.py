import sys

# This script processes a file of comma separated numbers
# For each line, it outputs two values. The first is the average of
# the number in the rows, the second is the average of all numbers
# up to and including the current row.

argv1 = sys.argv[1] # Filename of puzzle data passed as parameter

inputdata = open(argv1, "r").readlines()

print("Line Average,Total Average")

count_elements  = 0
sum_elements    = 0

for line in inputdata:

    count_line  = 0
    sum_line    = 0

    for element in line.split(','):

        count_line += 1
        sum_line += int(element)

        count_elements += 1
        sum_elements += int(element)

    print(f"{round(sum_line / count_line, 2)},{round(sum_elements / count_elements, 2)}")
