# importing the csv files
import csv
with open ('csv1.csv', 'r') as f:
    file1 = list(csv.reader(f))

with open('csv2.csv', 'r') as w:
    file2 = list(csv.reader(w))
