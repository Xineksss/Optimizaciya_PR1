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
    print("0 - Выход")

    choice = int(input("\nВаш выбор: "))

    if choice == 1:
        print("\nМетод деления отрезка пополам\n")
        result1, table1 = bisection(j0, 1, 5, 10**(-10))
        print_bisection_table(result1, table1)
        result2, table2 = bisection(j0, 3, 7, 10**(-10))
        print_bisection_table(result2, table2)
        print("\n\nМетод простой итерации\n")
        result3, table3 = iteration(j0, -1, 2, 10**(-10))
        print_iteration_table(result3, table3)
        result4, table4 = iteration(j0, 1, 5.3, 10**(-10))
        print_iteration_table(result4, table4)
        print("\n\nМетод Ньютона\n")
        result5, table5 = newton(j0, 2, 10**(-10))
        print_iteration_table(result5, table5)
        result6, table6 = newton(j0, 5, 10**(-10))
        print_iteration_table(result6, table6)

    elif choice == 2:
        print("\nМетод деления отрезка пополам\n")
        result1, table1 = bisection(j1, 3, 5, 10**(-10))
        print_bisection_table(result1, table1)

        result2, table2 = bisection(j1, 6, 8, 10**(-10))
        print_bisection_table(result2, table2)

        print("\n\nМетод простой итерации\n")
        result3, table3 = iteration(j1, -1, 3.5 , 10**(-10))
        print_iteration_table(result3, table3)

        result4, table4 = iteration(j1, 1, 7, 10**(-10))
        print_iteration_table(result4, table4)

        print("\n\nМетод Ньютона\n")
        result5, table5 = newton(j1, 3, 10**(-10))
        print_iteration_table(result5, table5)

        result6, table6 = newton(j1, 6, 10**(-10))
        print_iteration_table(result6, table6)


    elif choice == 3:
        print("\nМетод деления отрезка пополам\n")
        result1, table1 = bisection(y0, 0.5, 1.5, 10**(-10))
        print_bisection_table(result1, table1)

        result2, table2 = bisection(y0, 3, 5, 10**(-10))
        print_bisection_table(result2, table2)

        print("\n\nМетод простой итерации\n")
        result3, table3 = iteration(y0, 0.5, 1, 10**(-10))
        print_iteration_table(result3, table3)

        result4, table4 = iteration(y0, -1, 4, 10**(-10))
        print_iteration_table(result4, table4)

        print("\n\nМетод Ньютона\n")
        result5, table5 = newton(y0, 1, 10**(-10))
        print_iteration_table(result5, table5)

        result6, table6 = newton(y0, 4, 10**(-10))
        print_iteration_table(result6, table6)


    elif choice == 4:
        print("\nМетод деления отрезка пополам\n")
        result1, table1 = bisection(y1, 1.5, 3, 10**(-10))
        print_bisection_table(result1, table1)

        result2, table2 = bisection(y1, 5, 6, 10**(-10))
        print_bisection_table(result2, table2)

        print("\n\nМетод простой итерации\n")
        result3, table3 = iteration(y1, 1, 2, 10**(-10))
        print_iteration_table(result3, table3)

        result4, table4 = iteration(y1, -0.5, 5.5, 10**(-10))
        print_iteration_table(result4, table4)

        print("\n\nМетод Ньютона\n")
        result5, table5 = newton(y1, 2, 10**(-10))
        print_iteration_table(result5, table5)

        result6, table6 = newton(y1, 5.5, 10**(-10))
        print_iteration_table(result6, table6)

    elif choice == 0:
        break

    input("\nНажмите Enter, чтобы вернуться в меню...")