def iteration(f, lam, x0, eps):
    table = []
    count = 0

    while True:
        xn = x0 - lam * f(x0)
        tolerance = abs(xn - x0)
        table.append([count, xn, tolerance])

        if abs(xn - x0) < eps:
            return xn, table

        x0 = xn
        count += 1
