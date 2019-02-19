from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import random
import inspect

curve_points  = {}
random_points = {"x" : [], "y" : []}
max_curve_y   = 0

def draw_function(fun, a, b, total_points):
    curve_points["x"] = np.linspace(a, b, total_points)
    curve_points["y"] = fun(curve_points["x"])
    plt.plot(curve_points["x"], curve_points["y"])

def create_random_points(total_points, a, b, max):
    for counter in range(total_points):
        random_points["x"].append(random.uniform(a, b))
        random_points["y"].append(random.uniform(0, max))

def draw_random_points():
    plt.plot(random_points["x"], random_points["y"], 'rx')

def calculate_points_below_curve(fun):
    points_below = 0
    for x, y in zip(random_points["x"], random_points["y"]):
        if y < fun(x):
            points_below = points_below + 1

    return points_below

def mc_integration(fun, a, b, total_points=10000):
    draw_function(fun, a, b, total_points)
    max_curve_y = np.amax(curve_points["y"])
    create_random_points(total_points, a, b, max_curve_y)
    draw_random_points()

    print("---")
    print("::: Function: {}::: Limits of Integration: {} and {}\n::: Total Random Points:   {}\n".format(inspect.getsource(fun).replace("    ", ""), a, b, total_points))
    print("::: Integration calc with Monte Carlo method:      {}".format(round((calculate_points_below_curve(fun)/total_points)*(b-a)*max_curve_y, 3)))
    print("::: Integration calc with ScyPy 'quad' function:   {}".format(round(quad(fun, a, b)[0], 3)))
    print("---")

    plt.axis([a, b, 0, max_curve_y])
    plt.show()

def main():
    mc_integration(lambda x: x ** 2, 0, 3, 5000)

#------------------------#

main()
