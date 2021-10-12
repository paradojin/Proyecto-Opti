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

def funcion_objetivo(mat,oferta,demanda):
    fo=""
    rest_of=""
    rest_dem=""
    contador=0
    list_new=list()
    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])) :
            if fo == "":
                fo= "Min = " + str(mat[i][j])+"*x"+ str(i+1) + str(j+1)
                
            
            else:
                fo= fo + " + "+ str(mat[i][j])+"*x"+ str(i+1) + str(j+1)
                
            
    fo=fo +";"+"\n"
    
    for a in range(0,len(oferta)):
        contador=0
        for b in range(0,len(demanda)) :
    
            if contador == len(demanda)-1:
               
                rest_of =rest_of+"x"+ str(a+1) + str(b+1) +" <= "+ str(oferta[a])+";\n"
                
            else:
                 rest_of =rest_of+"x"+ str(a+1) + str(b+1)+" + " 
                 contador+=1
    
    for c in range(0,len(demanda)):
        cont=0
        for d in range(0,len(oferta)):
            if cont == len(oferta)-1:
                rest_dem=rest_dem +"x"+ str(d+1) + str(c+1) +" >= "+ str(demanda[c])+";\n"
            else:
                rest_dem =rest_dem+"x"+ str(d+1) + str(c+1)+" + " 
                cont+=1
                


    return fo+"\n"+rest_of+rest_dem

def crear_archivo(funcion):
    archivo= open("Modelo Transporte.lg4","w") 
    archivo.write(funcion)  
    archivo.close

    

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
    
    
    
    #problemSize = random.randint(1,3)
    problemSize = 0
    
    # 0: Muy pequeño
    # 1: Pequeño
    # 2: Mediano
    # 3: Grande

    # Casos inicialmente considerados Oferta = Demanda y Oferta > Demanda
    if problemSize == 0:
        nplantas = random.randint(1,9)
        nreceptores =random.randint(1,9)
    elif problemSize == 1:
        nplantas = random.randint(10,15)
        nreceptores = random.randint(10,15)
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


    #print(sum(oferta))
    #print(sum(demanda))
    #print(cost_matrix)

    
    funcion=funcion_objetivo(cost_matrix,oferta,demanda)
    print(funcion)
    crear_archivo(funcion)
    

    #print_matrix(cost_matrix)



generate_problem()
    
