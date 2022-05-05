import csv
import matplotlib.pyplot as plt

def gather_data(n = 1):
    with open("eve_data.csv", "w") as file:
        csv_writer = csv.writer(file)
        for i in range(n):
            h = float(input("Enter height: "))
            w = float(input("Enter weight: "))
            csv_writer.writerow([h, w])


def retrieve_data():
    with open("eve_data.csv") as file:
        heights = []
        weights = []
        csv_reader = csv.reader(file)
        for row in csv_reader:
            heights.append(float(row[0]))
            weights.append(float(row[1]))
    return heights, weights

def graphs():
    x, y = retrieve_data()
    plt.plot(x, y, "go")
    plt.show()


graphs()