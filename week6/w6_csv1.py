import csv
with open('studentcity.csv', 'r') as file:
  reader = csv.reader(file)  
  reader = csv.DictReader(file)
  #reader = csv.reader(file, delimiter = '\t')
  for row in reader:
    print(row)