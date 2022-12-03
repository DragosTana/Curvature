import matplotlib.pyplot as plt
import csv
import numpy as np
import circle_fit as cf
def plot_track(data):
    x, y = data.T
    fig, ax = plt.subplots()
    ax.set_title("Dati")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.scatter(x, y, marker=".")
    plt.show()
def plot_curvature(curvature):
    x = list(range(len(curvature)))
    fig, ax = plt.subplots()
    ax.plot(x, curvature)
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

def calculate_curvature(track, n):
    curvature = []
    for i in range(n, len(track)-n):
        points = track[i-n:i+n+1]
        _,_,r,_ = cf.least_squares_circle(points)
        curvature.append(1/r)

    return curvature


def main():
    data = load_csv("Pista.csv")
    data = np.array(data)
    plot_track(data)
    curvature = calculate_curvature(data, 2)
    plot_curvature(curvature)
main()

