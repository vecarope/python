
notas = []
i=1
salir = False 
while(not salir):
    for n in range(5):
        notas.append(float(input(f"Ingrese nota nº {n+1}, en escala del 1 al 10 : ")))
    print(*notas)

    promedio= sum(notas)/len(notas)
    print("El promedio de nota es:",promedio)

    notaAlta = max(notas)
    print('La nota mas alta:',notaAlta)

    notaBaja = min(notas)
    print("La nota mas baja es:",notaBaja)
    respuesta = input("¿Quiere ingresar notas de otro alumno? (S/N)")
    if( respuesta == "N") or(respuesta =="n"):
        salir = True 
print("Adios")   
