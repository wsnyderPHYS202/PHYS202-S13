import numpy as np

def pointPotential(x,y,q,posx,posy):
    """This function will take in the paramaters of position and charge and return the voltage due to that charge"""
    from math import sqrt
    k = 8.99*10**9
    Vxy = (k*q)/np.sqrt((x-posx)**2 + (y-posy)**2)
    return Vxy

def dipolePotential(x,y,q,d):
    """Returns the potential at (x,y) of a dipole with d being the distance between the charges and q being the charges"""
    V1 = pointPotential(x,y,q,-d/2,0.)
    V2 = pointPotential(x,y,q,d/2,0.)
    Vdp = V1 - V2
    return Vdp



