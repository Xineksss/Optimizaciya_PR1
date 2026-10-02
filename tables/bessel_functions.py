import scipy


j0 = lambda x: scipy.special.jv(0, x)
j1 = lambda x: scipy.special.jv(1, x)
y0 = lambda x: scipy.special.yv(0, x)
y1 = lambda x: scipy.special.yv(1, x)