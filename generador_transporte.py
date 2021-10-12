import random


def print_matrix(matrix):
    # Imprimir costos en formato matriz
    
    rows = len(matrix)
    columns = len(matrix[0])

    text = ""
    for j in range(0,columns):
        text += "\t| " + str(j )
    print(text )
    print("--------"*(columns+1))

    for i in range(0,rows):
        text = str(i) + "\t|"
        for j in range(0,columns):
            text += " "+ str(matrix[i][j]) + "\t|"

        print(text)
    

def generate_matrix(i, j, value_limit):
    # Generar matriz, de tamaño i*j, con valores desde 0 hasta value_limit
    
    matrix = list()
    for h in range(0,i):
        line = list()
        for v in range(0,j):
            line.append(random.randint(0,value_limit))

        matrix.append(line)
    return matrix

def generate_random_list(size, a, b):
    # Generar lista de tamaño "size", con valores en un rango "a" y "b"

    return_list = list()

    for i in range(0,size):
        return_list.append(random.randint(a,b))
    return return_list  
    
def generate_random_list_sum(size, a, b, limit):

    random_list = list()
    last = 0

    while last <= 0:
        random_list.clear()
        for i in range(0,size - 1):
            random_list.append(random.randint(a,b))
        last = limit - sum(random_list)

    random_list.append(last)
    return random_list

def generate_problem():

    # PROBLEMA DE TRANSPORTE
    
    # ELEMENTOS NECESARIOS:
    #   - OFERTA DE PLANTAS
    #   - DEMANDA DE PRODUCTOS
    #   - COSTO POR UNITARIO POR TRANSPORTE

    # MINIMIZAR COSTO TOTAL, O MAXIMIZAR UTILIDADES ¿?g

    # RESTRICCIONES:
    #   - SATISFACER DEMANDA Y/O RESPETAR OFERTA(BALANCEADO O DESBALANCEADO)
    #   - SRS
    
    # --------------------------------------------------------------------------

    # Definir tamaño de la problematica
    
    problemSize = random.randint(1,3)
    
    # 1: Pequeño
    # 2: Mediano
    # 3: Grande

    if problemSize == 1:
        nplantas = random.randint(10,99)
        nreceptores = random.randint(10,99)
    elif problemSize == 2:
        nplantas = random.randint(100,999)
        nreceptores = random.randint(100,999)
    else:
        nplantas = random.randint(1000,9999)
        nreceptores = random.randint(1000,9999)

    cost_matrix = generate_matrix(nplantas, nreceptores, 100) # Costo unitario de transporte desde i hasta j.

    

    # Definicion a priori de la oferta y demanda
    oferta = generate_random_list(nplantas, 0, 100) # Lista de productos ofertados por cada planta
    demanda = generate_random_list(nreceptores, 0, 100) # Lista de productos solicitados por cada demandante

    balance_type = random.randint(1,3)

    # 1: of < de
    # 2: of == de
    # 3: of > de

    # print("balance type = ",balance_type)
    if balance_type == 1:
        while(sum(oferta) > sum(demanda)):
            oferta = generate_random_list(nplantas, 0, 100) # Lista de productos ofertados por cada planta
            demanda = generate_random_list(nreceptores, 0, 100) # Lista de productos solicitados por cada demandante
    elif balance_type == 2:
        oferta = generate_random_list(nplantas, 0, 100) # Lista de productos ofertados por cada planta
        demanda = generate_random_list_sum(nreceptores, 0, 100, sum(oferta))
    else:
        while(sum(oferta) < sum(demanda)):
            oferta = generate_random_list(nplantas, 0, 100) # Lista de productos ofertados por cada planta
            demanda = generate_random_list(nreceptores, 0, 100) # Lista de productos solicitados por cada demandante


    # --------------------------------------------------------------------------
    # El siguiente codigo limita la generacion a unicamente problemas factibles
    # , pero como se pide analizar infactibilidad se ignorará.
    
    #while(oferta < demanda):
        #demanda = generate_random_list(nreceptores, 0, 100)
    # --------------------------------------------------------------------------

    print("Problema de transporte, con "+str(nplantas)+ " plantas y "+str(nreceptores)+ " demandantes generado.")
    
    print("sum oferta "+str(sum(oferta))+" | sum demanda "+str(sum(demanda)))
    
    return (nplantas, nreceptores, oferta, demanda, cost_matrix)
    

generate_problem()
    
    
    
