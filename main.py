from graphs.print_graphs import print_graph
from tables.bisection_table import print_bisection_table
from tables.bessel_functions import *
from methods.bisection import bisection
from methods.iteration import iteration
from methods.newton import newton
from tables.iteration_table import print_iteration_table


while True:

    print("\nВыберите функцию:")
    print("1 - J0")
    print("2 - J1")
    print("3 - Y0")
    print("4 - Y1")
    print("5 - Посмотреть графики функций")
    print("0 - Выход")

    choice = input("\nВаш выбор: ")

    if choice == "0":
        break

    if choice == "":
        continue

    if choice not in ["1", "2", "3", "4", "5", "0"]:
        print("Неправильный выбор!!!")
        continue

    if choice == "5":
        print_graph()
        continue

    print("\nВыберите метод:")
    print("1 - Метод деления отрезка пополам")
    print("2 - Метод простой итерации")
    print("3 - Метод Ньютона")
    print("0 - Назад")

    method = input("\nВаш выбор: ")

    if method == "":
        continue

    if method == "0":
        continue


    eps = 10**(-10)


    if method == "1":

        print("\nМетод деления отрезка пополам\n")

        if choice == "1":
            result1, table1 = bisection(j0, 1, 5, eps)
            result2, table2 = bisection(j0, 3, 7, eps)

        elif choice == "2":
            result1, table1 = bisection(j1, 3, 5, eps)
            result2, table2 = bisection(j1, 6, 8, eps)

        elif choice == "3":
            result1, table1 = bisection(y0, 0.5, 1.5, eps)
            result2, table2 = bisection(y0, 3, 5, eps)

        elif choice == "4":
            result1, table1 = bisection(y1, 1.5, 3, eps)
            result2, table2 = bisection(y1, 5, 6, eps)

        else:
            print("Неправильный выбор!!!")
            continue

        print_bisection_table(result1, table1)
        print_bisection_table(result2, table2)




    elif method == "2":

        print("\nМетод простой итерации\n")

        if choice == "1":
            result1, table1 = iteration(j0, -1, 2, eps)
            result2, table2 = iteration(j0, 1, 5.3, eps)

        elif choice == "2":
            result1, table1 = iteration(j1, -1, 3.5, eps)
            result2, table2 = iteration(j1, 1, 7, eps)

        elif choice == "3":
            result1, table1 = iteration(y0, 0.5, 1, eps)
            result2, table2 = iteration(y0, -1, 4, eps)

        elif choice == "4":
            result1, table1 = iteration(y1, 1, 2, eps)
            result2, table2 = iteration(y1, -0.5, 5.5, eps)

        else:
            print("Неправильный выбор!!!")
            continue

        print_iteration_table(result1, table1)
        print_iteration_table(result2, table2)


    elif method == "3":

        print("\nМетод Ньютона\n")

        if choice == "1":
            result1, table1 = newton(j0, 2, eps)
            result2, table2 = newton(j0, 5, eps)

        elif choice == "2":
            result1, table1 = newton(j1, 3, eps)
            result2, table2 = newton(j1, 6, eps)

        elif choice == "3":
            result1, table1 = newton(y0, 1, eps)
            result2, table2 = newton(y0, 4, eps)

        elif choice == "4":
            result1, table1 = newton(y1, 2, eps)
            result2, table2 = newton(y1, 5.5, eps)

        else:
            print("Неправильный выбор!!!")
            continue

        print_iteration_table(result1, table1)
        print_iteration_table(result2, table2)


    else:
        print("Неправильный выбор!!!")
        continue


    input("\nНажмите Enter, чтобы вернуться в меню...")