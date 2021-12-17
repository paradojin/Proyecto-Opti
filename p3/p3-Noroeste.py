from random import randint, randrange
import numpy as np
import time

def generar_lista_alea(n,q,var):
    lis= []
    i=1
    while i <= q :
        if q%2 != 0:
            if i == q:
                lis.append(n)
                break
        dif = randrange(var)
        lis.append(n - dif)
        lis.append(n + dif)
        i+=2
    return lis
    
# Funcion Objetivo
def fun_obj(xij,cij):
    suma = 0
    for i in range(I):
        for j in range(J):
            suma += xij[i][j]*cij[i][j]
    return suma

#Generacion de Parametros
I=int(input("Ingrese el numero de plantas: "))
J=int(input("Ingrese numero de centros de distribucion: ")) 
n_max=int(input("Suma de las capacidades: "))                             ##Este numero debe ser divisible por los inputs anteriores
ni=int(n_max/I)
nj=int(n_max/J)
var=int(input("Ingrese la variacion maxima de capacidad: "))              ##Este numero deber ser menor que el menor de los (inputs anteriores*100)
cij_inf=int(input("Ingrese el limite inferior de costo de transporte: "))
cij_sup=int(input("Ingrese el limite superior de costo de transporte: "))

inicio = time.time()


oi=generar_lista_alea(ni, I, var)     #se crea una lista auxiliar del costo de plantas
oi_aux = []
for o in oi:
    oi_aux.append(o)

dj=generar_lista_alea(nj, J, var)     #se crea una lista auxiliar del costo de los centros
dj_aux = []
for d in dj:
    dj_aux.append(d)

# Matriz de costos
cij=[]
cij_aux=[]
for i in range(I):
    list_aux= []
    for j in range(J):
        num = randint(cij_inf, cij_sup)
        list_aux.append(num)
    cij.append(list_aux)
    cij_aux.append(list_aux)

# Matriz de 0 c
xij= []
for i in range(I):
    list_aux= []
    for j in range(J):
        list_aux.append(0)
    xij.append(list_aux)



### Comienza el problema de esquina noroeste
print("Solucion factible Esquina Noroeste")
#Posicion inicial
i=0
j=0

while True:
    xij[i][j] = min(oi_aux[i],dj_aux[j])
    oi_aux[i] -= xij[i][j]
    dj_aux[j] -= xij[i][j]

    if oi_aux[i] < dj_aux[j]:
        i+=1
    elif oi_aux[i] > dj_aux[j]:
        j +=1
    else:
        i+=1
        j+=1
    if oi_aux[I-1] == 0 and dj_aux[J-1] == 0:
        break

print(np.array(xij))
val_fo=fun_obj(xij, cij)
print("valor objetivo = ", val_fo)
fin = time.time()
print("Tiempo de ejecucion: "+str(fin-inicio)+" [s]")






