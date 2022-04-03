from math import e
def punishmentFunction(x):
    sigmoid = 1-(2*( (1/(1+e**(-5*(1-x**0.7))) ) -0.5) )
    
    return sigmoid

    # firstPart = -(float(5)*(float(1)-x))

print(punishmentFunction(0.9))