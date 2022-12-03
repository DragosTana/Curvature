import matplotlib.pyplot as plt
import csv
import numpy as np

def plot_data_2D(data):
    x, y = data.T
    fig, ax = plt.subplots()
    ax.set_title("Dati")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.scatter(x, y, marker=".")
    plt.show()

def load_csv(file_name):
    data = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            point = []
            for word in line:
                point.append(float(word))
            data.append(point)
    return data

def main():
    data = load_csv("Pista.csv")
    data = np.array(data)
    plot_data_2D(data)

main()

