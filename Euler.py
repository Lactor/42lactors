#
# Implementation of the Euler's method and the Heun's method
# Author: Francisco Machado
#

def f(x): #derivative of x
    return x


def Euler( DT):
    path = "e"+str(DT)+".out"
    res = open(path, 'w' )
    x=1
    t = 0.
    while t <7:
        res.write(str(t) + " " + str(x)+ "\n")
        x += f(x)*DT
        t+=DT

def Heuns( DT):
    path = "h"+str(DT)+".out"
    res = open(path, 'w')
    x=1
    t=0.
    while t<7:
        res.write(str(t) + " " + str(x)+ "\n")
        k1 = f(x)*DT
        k2 = f(x+k1)*DT
        x+= 0.5*(k1+k2)
        t+=DT

Euler(1)
Euler(0.1)
Euler(0.01)
Euler(0.001)


Heuns(1)
Heuns(0.1)
Heuns(0.01)
Heuns(0.001)

