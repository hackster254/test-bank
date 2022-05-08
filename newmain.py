####the data lines
import pandas as pd 

with open("Input Text.txt", 'r') as temp_f:
    # get No of columns in each line
    col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(0, max(col_count))]

### Read csv
df = pd.read_csv("Input Text.txt", header=None, delimiter=":", names=column_names)

print(df)