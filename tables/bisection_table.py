def print_bisection_table(result, table):
    print("Итерация\tЗначение \t    Погрешность")
    print("-" * 60)

    for row in table:
        print(f"{row[0]:<9}", f"{row[1]:<20.12f}"[:12], " " * 4, f"{row[2]:<100.12f}"[:12])
    print("Корень:", f"{result}"[:12])


