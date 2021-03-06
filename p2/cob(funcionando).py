from random import randint
import random

def antena_existe(ant,antenas_repetidas):
    if (ant not in  antenas_repetidas):
        antenas_repetidas.append(ant)
        return 1
    return 0
    
Pais = []
antenas = []
costo = []

rango_inferior_regiones = int(
    input(" escriba el rango inferior minimo de regiones: "))
rango_superior_regiones = int(
    input(" escriba el rango superior maximo de regiones: "))
rango_inferior_antenas = int(
    input(" escriba el rango inferior minimo de antenas: "))
rango_superior_antenas = int(
    input(" escriba el rango superior maximo de antenas: "))

min_valor = int(input(" escriba minimo valor de coste de una antena: "))
max_valor = int(input(" escriba maximo valor de coste de una antena: "))

if(rango_inferior_antenas>rango_superior_antenas or rango_inferior_regiones > rango_superior_regiones or min_valor > max_valor):
    print("Los Limites ingresados se contradicen, vuelva a ejecutar")


regiones_creadas = random.randint(
    rango_inferior_regiones, rango_superior_regiones)   #este rango puede ser random o fijo 
print(" cantidad de regiones: " + str(regiones_creadas))

antenas_creadas = random.randint(
    rango_inferior_antenas, rango_superior_antenas) # este rango puede ser random o fijo
print(" cantidad de antenas: " + str(antenas_creadas))

#creando las antenas
for antena in range(antenas_creadas):
    antenas.append(str("X" + str(antena+1)))
    costo_antena=random.randint(min_valor,max_valor)
    costo.append(costo_antena)
# creando las regiones de nuestro pais 
for region in range(regiones_creadas):
    Pais.append(region+1)

# diccionario con llave la antena y el valor de cada antena son la regiones que ocupa 
diccionario=dict.fromkeys(antenas,[])

#repetidas para sacar las antenas que ocupan una misma area
repetidas=[]

auxiliar=Pais
for llave in diccionario:
    bandera=1
    while(bandera==1):
        antena_cobertura=randint(2, (regiones_creadas-1))
        coberturas_por_antena=[]
        for elem in range(antena_cobertura):
            anti_infactible=randint(1,(regiones_creadas-1))
            if (anti_infactible not in coberturas_por_antena):
                coberturas_por_antena.append(anti_infactible)
            else:
                elem=elem-1
        coberturas_por_antena=sorted(coberturas_por_antena)
        if (antena_existe(coberturas_por_antena,repetidas)):
            for elemento in coberturas_por_antena:
                if elemento in auxiliar:
                    auxiliar.remove(elemento)
            diccionario[llave]=coberturas_por_antena
            bandera=0
        
while (len(auxiliar)>0):
    verificacion=len(auxiliar)
    veri=random.choice(antenas)
    coberturas_antiguas= diccionario[veri]
    coberturas_antiguas.append(auxiliar[verificacion-1])
    coberturas_antiguas=sorted(coberturas_antiguas)
    auxiliar.remove(auxiliar[verificacion-1])
    verificacion=verificacion-1

for clave in diccionario:
    zonas=diccionario[clave]
    print("Antena"+clave+ ": "+str(zonas))

print(auxiliar)
print(Pais)
print(antenas)
print(costo)
print(diccionario)
############################ lindo #########################

funcion_objetivo=""
restricciones=[]
variables_enteras=[]
contador=0

for key in diccionario:
    funcion_objetivo=funcion_objetivo+str(costo[contador])+"*"+key+" + "
    variables_enteras.append(key)
    contador+=1

for regiones in range(regiones_creadas):
        Pais.append(regiones+1)

for reg in Pais:
    antenaza=""
    for key in diccionario:
        if reg in diccionario[key]:
            antenaza=antenaza+key+" + "
    antenaza= antenaza[0:-2]
    antenaza=antenaza+">= 1;"
    restricciones.append(antenaza)

funcion_objetivo=funcion_objetivo[0:-2]
archivo=open("proyecto2.lg4","w")
archivo.write("min = "+funcion_objetivo+";\n\n")
for res in restricciones:
    archivo.write(res+"\n")

for variable in variables_enteras:
    archivo.write("@BIN ("+ variable+");\n")
archivo.close()

print(restricciones)
########################Minizinc###################
file=open("proyecto2.mzn","w")
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
    file.write("constraint "+re+"\n")
file.write("\n")
file.write("solve minimize variable_obj;")
file.close()