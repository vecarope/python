notas=[]
num_notas= int(input("cuantas notas quiere ingresar"))
suma=0
i=1

while(i<= notas):
    nota=float(input("Ingese la nota",i))
    suma=suma+nota
    i+=1
    prom=suma/n
    print("El promedio de nota es:",prom)
