import csv
file = open("updatedpage.csv")
csvreader = csv.reader(file)
header = next(csvreader)
header.pop(0)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()