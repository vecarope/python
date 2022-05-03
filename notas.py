#Notas de alumnos
#Preguntar n de notas 
#Ingresar cada nota (con decimales)
#Regresar cuantas notas están sobre o son mayores del promedio de notas

notas = []
i=1
cantidadNotas=int(input("Cuantas notas quiere ingresar?"))
for n in range(cantidadNotas):
    notas.append(float(input(f"nota nº {n+1} : ")))
print(notas)
promedio= sum(notas)/len(notas)
print("El promedio es:",promedio)
print( len([n for n in notas if n > promedio]), "notas son mayores que el promedio")
