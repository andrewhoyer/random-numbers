# Random Number Analysis

A collection of scripts that verify, process, and analyse data. 

## Verify

Each data file consists of lines of ten comma-separated integers. Before analysing the data, use this script to verify it is in the correct format.

For example, to verify the file containing random numbers from the D12, run this command:

```python3 verify-format.py ../data/d12.csv```

## Analysis

### Averages

This script processes each line in a data file, and outputs the average of the numbers in the line, and the average of all numbers processed up to and including that line.

```python3 averages.py ../data/d12.csv```
