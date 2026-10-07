def bisection(f, a, b, eps):
    result = []
    count = 0
    while True:
        if (b - a) < eps:
            return c, result

        c = (a + b) / 2
        tolerance = (b - a) / 2


        result.append([count, c, tolerance])

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        count += 1
