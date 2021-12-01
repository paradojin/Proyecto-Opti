import os

def generar_problema(estados_variables, tope, n_antenas, coberturas, costos):

    if estados_variables[0]:
        print("Generar random n°")
    if estados_variables[1]:
        print("Cobertura random")
    if estados_variables[2]:
        print("Costos random")

    input("Problema generado en .... Presione cualquier tecla p")



nombre_variables = ["N° antenas", "Cobertura antenas", "Costo instalar"]
estado_aleatorio_variables = [True, True, True]
n_antenas = 0
cobertura = dict()
costos = list()
    

while(True):
    _=os.system("clear")
    print("Estado actual de las variables:")

    for i in range(1, len(estado_aleatorio_variables) + 1):
    
        if i-1 == 1:
            if estado_aleatorio_variables[0]:
                print("\t",i,"[Desactivado] "+nombre_variables[i-1])
            else:
               print(i,"[Random] "+nombre_variables[i-1]) if estado_aleatorio_variables[i-1] else print(i,"[Fijado] "+nombre_variables[i-1])
            
        else:
            print(i,"[Random] "+nombre_variables[i-1]) if estado_aleatorio_variables[i-1] else print(i,"[Fijado] "+nombre_variables[i-1])
    
    print("Presione Enter para generar la instancia, o ingrese el numero de la variable a definir/indefinir: ")
    
    test = input()
    
    if (test == ""):
        generar_problema(estado_aleatorio_variables, 10, n_antenas, cobertura, costos)
    elif (int(test) < len(estado_aleatorio_variables) + 1 and int(test) > 0 ):
        
        if int(test) == 1 and estado_aleatorio_variables[int(test)-1]:
            print("Ingrese el n° de antenas: ")
            n_antenas = int(input())

        if int(test) == 2 and not estado_aleatorio_variables[0] and  estado_aleatorio_variables[int(test)-1]:
            cobertura.clear()
            estado_aleatorio_variables[1] = True
            for numero_antena in range(1,n_antenas+1):
                print("Ingrese las zonas que cubre la antena n°",numero_antena,": ")
                cobertura[numero_antena] = list(map(int, input().split(" "))) # MODIFICAR

        if int(test) == 3 and estado_aleatorio_variables[int(test)-1]:
            print("Ingrese el costo asociado a las antenas: ")
            n_antenas = int(input()) # MODIFICAR

        estado_aleatorio_variables[int(test) - 1] = not estado_aleatorio_variables[int(test) - 1]
        if estado_aleatorio_variables[0]: estado_aleatorio_variables[1] = True # Lock aleatoriedad de coberturas si no hay n° definido.

    