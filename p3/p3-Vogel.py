from random import randint, randrange
import numpy as np
import time

def generador_lista_aleatoria(n, q, var):
    lista = []
    i = 1
    while i <= q:
        if (q % 2 != 0):
            if (i == q):
                lista.append(n)
                break
        dif = randrange(var)
        lista.append(n-dif)
        lista.append(n+dif)
        i += 2
    return lista

def fun_obj(xij, cij):
    suma = 0
    for i in range(I):
        for j in range(J):
            suma += xij[i][j]*cij[i][j]
    return suma


def obtener_fila_min_costo(max_pen_i, n_pen_i, pen_i, cij_aux, cij_sup, I, J):
    min_costo = cij_sup+1
    i_selec = 0
    for i in range(I):
        if pen_i[i] == max_pen_i:
            for j in range(J):
                costo = cij_aux[i][j]
                if costo < min_costo and costo != True:
                    min_costo = costo
                    i_selec = i
    return i_selec


def obtener_columna_min_costo(max_pen_j, n_pen_j, pen_j, cij_aux, cij_sup, J, I):
    min_costo = cij_sup+1
    j_selec = 0
    for j in range(J):
        if pen_j[j] == max_pen_j:
            for i in range(I):
                costo = cij_aux[i][j]
                if costo < min_costo and costo != True:
                    min_costo = costo
                    j_selec = i
    return j_selec

# generacion de parametros

I = int(input('ingrese el numero de plantas: '))
J = int(input('ingrese el numero de centros de distribucion: '))
n_max = int(input('suma de las capacidades: '))                        ##Este numero debe ser divisible por los inputs anteriores
ni = int(n_max/I)
nj = int(n_max/J)
Var = int(input('variacion maxima de  capacidad: '))                   ##Este numero deber ser menor que el menor de los (inputs anteriores*100) 
cij_inf = int(input('ingrese el numero inferior del costo de transporte: '))
cij_sup = int(input('ingrese el numero superior del costo de transporte: '))

inicio = time.time()

oi = generador_lista_aleatoria(ni, I, Var)
oi_auxiliar = []
for o in oi:
    oi_auxiliar.append(o)

dj = generador_lista_aleatoria(nj, J, Var)
dj_auxiliar = []
for d in dj:
    dj_auxiliar.append(d)


cij = []
cij_auxiliar = []
for i in range(I):
    lista_aux1 = []
    lista_aux2 = []
    for j in range(J):
        num = randint(cij_inf, cij_sup)
        lista_aux1.append(num)
        lista_aux2.append(num)
    cij.append(lista_aux1)
    cij_auxiliar.append(lista_aux2)

# generacion estructura de variables
xij = []
k = 0
for i in range(I):
    lista_aux = []
    for j in range(J):
        lista_aux.append(0)
    xij.append(lista_aux)

# funcion objetivo


pen_i = list(np.ones(I))
pen_j = list(np.ones(J))
flag_i = True
flag_j = True

while True:
    arr = np.array(cij_auxiliar)
    if flag_i == True:
        for i in range(I):
            j_menor = 0
            min_costo1 = cij_sup+1
            min_costo2 = cij_sup+1
            if pen_i[i] != -1:
                for j in range(J):
                    if cij_auxiliar[i][j] < min_costo1 and cij_auxiliar[i][j] != True:
                        min_costo1 = cij_auxiliar[i][j]
                        j_menor = j
                for j in range(J):
                    if cij_auxiliar[i][j] < min_costo1 and cij_auxiliar[i][j] != True and j != j_menor:
                        min_costo2 = cij_auxiliar[i][j]
                pen_i[i] = min_costo2-min_costo1

    if flag_j == True:
        for j in range(J):
            i_menor = 0
            min_costo1 = cij_sup+1
            min_costo2 = cij_sup+1
            if pen_i[i] != -1:
                for i in range(I):
                    if cij_auxiliar[i][j] < min_costo1 and cij_auxiliar[i][j] != True:
                        min_costo1 = cij_auxiliar[i][j]
                        i_menor = i
                for j in range(J):
                    if cij_auxiliar[i][j] < min_costo1 and cij_auxiliar[i][j] != True and i != i_menor:
                        min_costo2 = cij_auxiliar[i][j]
                pen_i[i] = min_costo2-min_costo1


    max_pen_i = np.array(pen_i).max()
    n_pen_i = pen_i.count(max_pen_i)
    max_pen_j = np.array(pen_j).max()
    n_pen_j = pen_j.count(max_pen_j)
    min_costo = cij_sup+1
    min_costo_fila = cij_sup+1
    min_costo_columna = cij_sup+1

    if max_pen_i > max_pen_j:
        if n_pen_i == 1:
            i_selec = pen_i.index(max_pen_i)
        else:
            i_selec = obtener_fila_min_costo(
                max_pen_i, n_pen_i, pen_i, cij_auxiliar, cij_sup, I, J)
        for j in range(J):
            if cij_auxiliar[i_selec][j] < min_costo and cij_auxiliar[i_selec][j] != True:
                min_costo = cij_auxiliar[i_selec][j]
        j_selec = cij_auxiliar[i_selec].index(min_costo)
    elif max_pen_i < max_pen_j:
        if n_pen_j == 1:
            j_selec = pen_j.index(max_pen_j)
        else:
            j_selec = obtener_columna_min_costo(
                max_pen_j, n_pen_j, pen_j, cij_auxiliar, cij_sup, J, I)
            for i in range(I):
                if cij_auxiliar[i][j_selec] < min_costo and cij_auxiliar[i][j_selec] != True:
                    min_costo = cij_auxiliar[i][j_selec]
        i_selec = list(np.array(cij_auxiliar)[:, j_selec]).index(min_costo)
    elif max_pen_i == max_pen_j:
        if pen_i > 1:
            i_canditato = obtener_fila_min_costo
        else:
            i_canditato = pen_i.index(max_pen_i)
        if pen_j > 1:
            j_canditato = obtener_columna_min_costo
        else:
            j_canditato = pen_j.index(max_pen_j)
        for j in range(J):
            if cij_auxiliar[i_canditato][j] < min_costo_fila and cij_auxiliar[i_canditato][j] != True:
                min_costo_fila = cij_auxiliar[i_canditato][j]
        j_posible = cij_auxiliar[i_canditato].index(min_costo_fila)
        for i in range(I):
            if cij_auxiliar[i][j_canditato] < min_costo_columna and cij_auxiliar[i][j_canditato] != True:
                min_costo_columna = cij_auxiliar[i][j_canditato]
        i_posible = list(np.array(cij_auxiliar)[:, j_canditato]).index(min_costo_columna)
        if min_costo_fila < min_costo_columna:
            i_selec = i_canditato
            j_selec = j_posible
        else:
            j_selec = j_canditato
            i_selec = i_posible

    xij[i_selec][j_selec] = min(oi_auxiliar[i_selec], dj_auxiliar[j_selec])
    oi_auxiliar[i_selec] -= xij[i_selec][j_selec]
    dj_auxiliar[j_selec] -= xij[i_selec][j_selec]
    if oi_auxiliar[i_selec] < dj_auxiliar[j_selec]:
        pen_i[i_selec] = -1
        for j in range(J):
            cij_auxiliar[i_selec][j] = True
        flag_i = False
        flag_j = True
    elif oi_auxiliar[i_selec] > dj_auxiliar[j_selec]:
        pen_j[i_selec] = -1
        for i in range(I):
            cij_auxiliar[i][j_selec] = True
        flag_i = True
        flag_j = False
    else:
        pen_i[i_selec] = -1
        pen_j[j_selec] = -1
        for j in range(J):
            cij_auxiliar[i_selec][j] = True
        for i in range(I):
            cij_auxiliar[i][j_selec] = True
        flag_i = True
        flag_j = True
    if np.array(oi_auxiliar).sum() == 0 and np.array(dj_auxiliar).sum() == 0:
        break
print(np.array(xij))
valor = fun_obj(xij, cij)
print(" el valor de la funcion objetivo es:", valor)
fin = time.time()
print("Tiempo de ejecucion: "+str(fin-inicio)+" [s]")
