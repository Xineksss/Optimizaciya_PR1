def print_newton_table(result, table):
    print("Итерация\tЗначение \t\t\t    Погрешность")
    print("-" * 60)

    for row in table:
        print(f"{row[0]:<10}{row[1]:<25.12f}{row[2]:<25.12f}")

    print("Корень:", result)