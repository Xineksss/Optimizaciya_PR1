import matplotlib.pyplot as plt, numpy as np
from tables.bessel_functions import *

def print_graph():
    print("\nВыберите функцию для построения графика:")
    print("1 - J0")
    print("2 - J1")
    print("3 - Y0")
    print("4 - Y1")
    print("0 - Назад")

    graph = input("\nВаш выбор: ")

    x_values = np.linspace(0.01, 20, 1000)

    if graph == "1":
        y = j0(x_values)
        name = "J0(x)"

    elif graph == "2":
        y = j1(x_values)
        name = "J1(x)"

    elif graph == "3":
        y = y0(x_values)
        name = "Y0(x)"

    elif graph == "4":
        y = y1(x_values)
        name = "Y1(x)"

    else:
        print("Неправильный выбор!!!")
        return

    plt.plot(x_values, y)
    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()