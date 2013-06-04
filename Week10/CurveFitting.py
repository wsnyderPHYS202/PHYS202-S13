def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slope and intercept
    paramers of the best fit line with their uncertainties."""
    n = 1./(x.size)
    pxy = n*sum(x*y)
    px = n*sum(x)
    py = n*sum(y)
    pxsq = n*sum((x**2))
    
    m = (pxy - px*py)/(pxsq - px**2)
    b = (pxsq*py - px*pxy)/(pxsq - px**2)
    
    pd = n*sum((y - (m*x+b))**2)
    unm = sqrt(1./(x.size - 2)*pd/(pxsq-px**2))
    unb = sqrt(1./(x.size - 2)*pd*pxsq/(pxsq-px**2))
    
    return m,b,unm,unb

def WeightedLinearLeastSquaresFit(x,y,w):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
    perform a weighted linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties."""
    W = float(sum(w))
    WXY = float(sum(w*x*y))
    WX = float(sum(w*x))
    WY = float(sum(w*y))
    WXsq = float(sum(w*(x**2)))
    
    m = (W*WXY-WX*WY)/(W*WXsq-(WX**2))
    b = (WXsq*WY-WX*WXY)/(W*WXsq-(WX)**2)
    
    unm = sqrt(W/(W*WXsq-(WX**2))) 
    unb = sqrt(WXsq/(W*WXsq-(WX**2)))
    
    return m,unm,b,unb


