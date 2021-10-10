import random

def print_matrix(matrix):
    
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
    matrix = list()
    for h in range(0,i):
        line = list()
        for v in range(0,j):
            line.append(random.randint(0,value_limit))

        matrix.append(line)
    return matrix

def generate_random_list(size, a, b):

    return_list = list()

    for i in range(0,size):
        return_list.append(random.randint(a,b))
    return return_list  
    

def generate_problem ():

    # PROBLEMA DE TRANSPORTE
    
    # ELEMENTOS NECESARIOS:
    #   - OFERTA DE PLANTAS
    #   - DEMANDA DE PRODUCTOS
    #   - COSTO POR UNITARIO POR TRANSPORTE
    #   - RUTAS HABILITADAS (PARA PROBLEMA MIXTO DE TRANSPORTE)

    # MINIMIZAR COSTO TOTAL, O MAXIMIZAR UTILIDADES ¿?

    # RESTRICCIONES:
    #   - SATISFACER DEMANDA Y/O RESPETAR OFERTA(BALANCEADO O DESBALANCEADO)
    #   - SRS
    
    
    
    problemSize = random.randint(1,3)
    
    # 1: Pequeño
    # 2: Mediano
    # 3: Grande

    # Casos inicialmente considerados Oferta = Demanda y Oferta > Demanda

    if problemSize == 1:
        nplantas = random.randint(10,99)
        nreceptores = random.randint(10,99)
    elif problemSize == 2:
        nplantas = random.randint(100,999)
        nreceptores = random.randint(100,999)
    else:
        nplantas = random.randint(1000,9999)
        nreceptores = random.randint(1000,9999)

    cost_matrix = generate_matrix(nplantas, nreceptores, 100)
    unitary_matrix  = generate_matrix(nplantas, nreceptores, 1) # Binarios
    
    oferta = generate_random_list(nplantas, 0, 100)
    demanda = generate_random_list(nreceptores, 0, 100)

    # ¿Casos de sobredemanda no resolubles?

    while(oferta < demanda):
        demanda = generate_random_list(nreceptores, 0, 100)

    # isMixed = True if random.randint(0,1) else False Definir


    print(sum(oferta))
    print(sum(demanda))





generate_problem()
    
    
    
