import csv
with open('movie3.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(["SN", "Movie", "Character"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])