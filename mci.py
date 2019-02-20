from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import random
import inspect

def calculate_function_between_limits(fun, a, b, total_points, using_numpy):
    fp = {}
    if using_numpy:
        fp["x"] = np.linspace(a, b, total_points)
        fp["y"] = fun(fp["x"])
    else:
        interval = (b - a) / total_points
        fp["x"], fp["y"] = [], []
        for counter in range(total_points):
            fp["x"].append(counter * interval)
            fp["y"].append(fun(fp["x"][counter]))
    return fp

def get_max_y_from_function(y_points, using_numpy):
    fmy = 0
    if using_numpy:
        fmy = np.amax(y_points)
    else:
        fmy = max(y_points)
    return fmy

def create_random_points(total_points, a, b, max, using_numpy):
    if using_numpy:
        rp = {}
        rp["x"] = np.random.uniform(a, 3 + 0.0001, total_points)
        rp["y"] = np.random.uniform(a, max + 0.0001, total_points)
    else:
        rp = {"x" : [], "y" : []}
        for counter in range(total_points):
            rp["x"].append(random.uniform(a, b))
            rp["y"].append(random.uniform(0, max))
    return rp

def calculate_points_below_function(fun, random_points, using_numpy):
    points_below = 0
    if using_numpy:
        points_below = sum(random_points["y"] < fun(random_points["x"]))
    else:
        for x, y in zip(random_points["x"], random_points["y"]):
            if y < fun(x):
                points_below = points_below + 1
    return points_below

def mc_integration(fun, a, b, total_points=10000, using_numpy=False):
    function_points  = calculate_function_between_limits(fun, a, b, total_points, using_numpy)
    function_max_y   = get_max_y_from_function(function_points["y"], using_numpy)
    random_points    = create_random_points(total_points, a, b, function_max_y, using_numpy)

    #PRINTING THE RESULTS
    print("---")
    print("::: Function: {}".format(inspect.getsource(fun).replace("    ", "")))
    print("::: Limits of Integration: {} and {}".format(a, b))
    print("::: Total Random Points:   {}".format(total_points))
    print("")
    print("::: Integration calc with Monte Carlo method:      {}".format(round((calculate_points_below_function(fun, random_points, using_numpy)/total_points)*(b-a)*function_max_y, 3)))
    print("::: Integration calc with ScyPy 'quad' function:   {}".format(round(quad(fun, a, b)[0], 3)))
    print("")
    print("::: Working with NumPy: {}".format(using_numpy))
    print("---")

    #VISUALIZATION OF THE RESULTS
    plt.plot(random_points["x"], random_points["y"], 'rx')
    plt.plot(function_points["x"], function_points["y"])
    plt.axis([a, b, 0, function_max_y])
    plt.show()

def main():
    mc_integration(lambda x: x ** 2, 0, 3, 10000, True)

#------------------------#

main()
