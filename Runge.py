

def f(x): #derivative of x
    return x


def Runge( DT):
    path = "r"+str(DT)+".out"
    res = open(path, 'w' )
    x=1
    t = 0.
    while t <7:
        res.write(str(t) + " " + str(x)+ "\n")
        k1 = f(x)*DT
        k2 = f(x+0.5*k1) *DT
        k3 = f(x+0.5*k2) *DT
        k4 = f(x+k3) * DT
        x += 1./6 * (k1 + 2*k2 + 2*k3 + k4)
        t+=DT

Runge(1)
Runge(0.1)
Runge(0.01)
