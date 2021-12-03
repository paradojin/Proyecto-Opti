import random
import sys

def antena_no_procesada(ant,antenas_repetidas):
    if (ant not in  antenas_repetidas):
        antenas_repetidas.append(ant)
        return 1
    return 0


def obtener_restricciones(zonas, diccionario):

    restricciones=[]

    for reg in zonas:
        antenaza=""
        for clave in diccionario:
            if reg in diccionario[clave]:
                antenaza=antenaza+clave+" + "
        antenaza= antenaza[0:-2]
        antenaza= antenaza+">= 1"
        restricciones.append(antenaza)

    return restricciones


    

def generar_lindo(diccionario, costo, restricciones):
    funcion_objetivo=""
    variables_enteras=[]
    contador=0

    for value in diccionario:
        funcion_objetivo=funcion_objetivo+str(costo[contador])+value+" + "
        variables_enteras.append(value)
        contador+=1


    funcion_objetivo=funcion_objetivo[0:-2]
    archivo=open("p2-cobertura.tlx","w")
    archivo.write("min "+funcion_objetivo+"\n" )
    for res in restricciones:
        archivo.write(res+"\n")
    archivo.write("end\n")
    for variable in variables_enteras:
        archivo.write("gin "+ variable+"\n")
    archivo.close()
    print("Problema generado en \"p2-cobertura.tlx\"")



def generar_minizinc(antenas, costo, restricciones):
    file=open("p2-cobertura.mzn","w")
    file.write("%Problema cobertura \n\n")
    file.write("%Parametros\n")
    for antenna in antenas:
        file.write("var 0..1: "+antenna+ ";\n")
    file.write("var int: variable_obj;\n\n")
    funcion=""
    contador_minizinc=0
    for i in antenas:
        if (len(funcion)==0):
            funcion= str(costo[contador_minizinc])+"*"+str(i)
        else:
            funcion=funcion+" + "+str(costo[contador_minizinc])+"*"+str(i)
        contador_minizinc+=1
    file.write("constraint variable_obj = "+funcion+";\n\n")
    for re in restricciones:
        file.write("constraint "+re+";\n")
    file.write("\n")
    file.write("solve minimize variable_obj;")
    file.close()
    print("Problema generado en \"p2-cobertura.mzn\"")
    



################# MAIN #################

zonas = []
antenas = []
costo = []

# inputs -----------------------

rango_inferior_zonas = int(
    input("Ingrese el limite inferior de zonas a crear: "))
rango_superior_zonas = int(
    input("Ingrese el limite supeior de zonas a crear: "))
rango_inferior_antenas = int(
    input("Ingrese el limite inferior de antenas: "))
rango_superior_antenas = int(
    input("Ingrese el limite superior de antenas: "))

min_valor = int(input("Ingrese el limite inferior de costos de las antenas: "))
max_valor = int(input("Ingrese el limite superior de costos de las antenas: "))

if(rango_inferior_antenas>rango_superior_antenas or rango_inferior_zonas > rango_superior_zonas or min_valor > max_valor):
    sys.exit("Los Limites ingresados se contradicen, vuelva a ejecutar")

# Las variables se definen aleatorios si rango_inferior < rango_superior, pero si son iguales entonces son fijos.
# Cantidad de zonas y antenas a crear.
cantidad_zonas = random.randint(
    rango_inferior_zonas, rango_superior_zonas)   
print("Cantidad de zonas:", cantidad_zonas)

cantidad_antenas = random.randint(
    rango_inferior_antenas, rango_superior_antenas) 
print("Cantidad de antenas: ", cantidad_antenas)

# Crear antenas
for antena in range(cantidad_antenas):
    antenas.append(str("X" + str(antena+1)))
    costo_antena=random.randint(min_valor,max_valor)
    costo.append(costo_antena)

# Crear zonas
for num_zona in range(cantidad_zonas):
    zonas.append(num_zona+1) # Se parte con indice >= 1

# Diccionario con llave "antena" y el valor de cada antena son las zonas que ocupa 
diccionario=dict.fromkeys(antenas,[])

#repetidas para sacar las antenas que ocupan una misma area
repetidas= []
auxiliar=zonas.copy()

# Definir para cada antena las zonas que cubre
for llave in diccionario:

    while(True):
        # N° zonas cubiertas por antena
        antena_cobertura=random.randint(2, cantidad_zonas - 1) # Forzar a que cada antena cubra por lo menos 2 zonas.
        # De todas maneras se puede cambiar a 1, considerando una antena que cubra unicamente 1 zona.
        # Lo anterior fuerza a que debe existir por lo menos 2 zonas.

        coberturas_por_antena=[]
        for elem in range(antena_cobertura):

            # Escapar en caso de que hayan mas antenas que zonas. De lo contrario loop infinito.
            if len(coberturas_por_antena) == cantidad_zonas:
                break
            
            # Asignar zonas aleatorias no consideradas.
            zona_seleccionada=random.randint(1, cantidad_zonas - 1)

            if (zona_seleccionada not in coberturas_por_antena):
                coberturas_por_antena.append(zona_seleccionada)
            else:
                elem=elem-1

        coberturas_por_antena=sorted(coberturas_por_antena)

        # Verificar si ya se proceso la antena actual.
        if (antena_no_procesada(coberturas_por_antena,repetidas)):
            # Si no fue procesada agregar al diccionario.
            for elemento in coberturas_por_antena:
                if elemento in auxiliar:
                    auxiliar.remove(elemento)
            diccionario[llave]=coberturas_por_antena
            break

# Verificar que por lo menos todas las zonas tengan 1 antena que lo cubra.
while len(auxiliar)>0:
    verificacion=len(auxiliar)
    veri=random.choice(antenas)
    coberturas_antiguas= diccionario[veri]
    coberturas_antiguas.append(auxiliar[verificacion-1])
    coberturas_antiguas=sorted(coberturas_antiguas)
    auxiliar.remove(auxiliar[verificacion-1])
    verificacion=verificacion-1

# Imprimir antenas creadas, con zonas que cubren
print("-"*50)
for clave in diccionario:
    temp=diccionario[clave]
    print("Antena"+clave+ ": "+str(temp))
print("-"*50)

print("Problema creado. Generando archivos...")

restricciones = obtener_restricciones(zonas, diccionario)

######################### Generar LINDO #########################
generar_lindo(diccionario, costo, restricciones)

######################### Generar MINIZINC #########################
generar_minizinc(antenas, costo, restricciones)
