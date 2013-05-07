def finiteDifference(x,y):
    """Takes the derivative of y with respect to x using 2 points"""
    import numpy as np
    dydx = np.zeros(y.shape, float)
    dydx[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx

def fourPtFiniteDiff(x,y):
    """Takes the derivative of y with respect to x using 4 points"""
    dydx = finiteDifference(x,y)
    h = abs(x[1]-x[2])
    length = len(x[:-2])
    for i in range(2, length):
        dydx[i] = (y[i - 2] - 8*y[i - 1] + 8*y[i +1 ] - y[i + 2])/(12*h)
    return dydx
