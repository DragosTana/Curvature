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
    data = np.array(data)
    return data


def calculate_curvature_circle(track, n):
    # calculate the curvature using a least squares circle passing through 2n+1 points
    curvature = []
    for i in range(n, len(track)-n):
        points = track[i-n:i+n+1]
        _, _, r, _ = cf.least_squares_circle(points)
        curvature.append(1/r)
    return curvature


def calcluate_curvature_poly(track, n):
    # calculate the curvature using a least square polynomial passing through 2n+1 points
    curvature = []
    for i in range(n, len(track) - n):
        points = track[i - n:i + n + 1]
        xp, yp = points.T
        tx = list(range(len(xp)))
        ty = list(range(len(yp)))
        x_coeff = np.polyfit(xp, tx, 2)  # list of a_2, a_1, a_0
        y_coeff = np.polyfit(yp, ty, 2)  # list of b_2, b_1, b_0
        # print(xp, yp, tx, ty, x_coeff, y_coeff)
        k = (2*(x_coeff[1]*y_coeff[2]-x_coeff[2]*y_coeff[1]))/(((x_coeff[1]**2)+(y_coeff[1]**2))**(3/2))
        curvature.append(k)
    return curvature


def main():
    data = load_csv("Pista.csv")
    plot_track(data)
    # curvature1 = calculate_curvature_circle(data, 2)
    # plot_curvature(curvature1)
    curvature2 = calcluate_curvature_poly(data, 2)
    plot_curvature(curvature2)


main()

