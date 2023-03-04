import numpy as np


nfil = int(input("Cuantos Dias: "))
ncol = int(input("Cuantas Vacas: "))
M = np.zeros((nfil, ncol))

for i in range(nfil):
    for j in range(ncol):
        M[i][j] = int(input("Cantidad de litros de leche: dia[" + str(i + 1) + "] vaca[" + str(j + 1) + "] = "))
print("*" * 50)

def sumDaily():
    Sume = lambda M: [ sum(i) for i in M]
    x = Sume(M)
    y = []
    y = np.zeros(nfil)
    
    print("Produccion diaria: ", x)

    for i in range(nfil):
        print("Produccion de Leche el dia " + str(i + 1) + ": " + str(x[i]))

    zz = max(x)
    yy = x.index(zz)  
    print("El dia que mas recogio leche fue " + str(yy + 1))

    for i in range(nfil):
        print(M[i])
        z = max(M[i])
        w = list(M[i])
        y[i] = w.index(z)
        print("*" * 50)
        print('w =', w)
        print('y =', y)

    print("*" * 50)

    for i in range(nfil):
        print("El " + str(i + 1) + " dia la vaca que mas dio leche fue = " + str(int(y[i]) + 1))



sumDaily()