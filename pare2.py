
num = []
i=0
salir = False
print("Pares e Impares")

while ( not salir):
    
    numero= int(input("Ingrese un número entre 1 y 100 :"))
    
    if numero <= 0 or numero >= 101:
        print ("Ingrese un numero mayor a 0 y menor a 100")
    
    elif numero % 2 == 0:
        print ( numero,"es un numero par")
        for i in range(numero+2, 101,+2):
            num.append(i)
        print("Los números pares siguientes son :",*num)
    else:
        print ( numero,"es un numero impar")
        for i in range(numero+2, 101,+2):
            num.append(i)
        print("Los números impares siguientes son:",*num)
    num.clear()
    respuesta = input("¿Quiere ingresar otro numero? (S/N)")
    if( respuesta == "N") or(respuesta =="n"):
        salir = True 
print("Adios")       