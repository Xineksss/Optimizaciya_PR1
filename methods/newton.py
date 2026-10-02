import scipy


def newton(f, x0, eps):
    table = []
    count = 0
    while True:
        df = scipy.differentiate.derivative(f, x0).df
        xn = x0 - (f(x0) / df)
        tolerance = abs(xn - x0)
        table.append([count, xn, tolerance])

        if abs(xn - x0) < eps:
            return xn, table

        x0 = xn
        count += 1