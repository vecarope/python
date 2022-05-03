agenda = {}

salir = False
print(" Bienvenido a Agenda")

while ( not salir):
    
    nombre= input("ingrese un nombre:")
    telefono = int(input("ingrese un telefono: "))
    
    if (nombre not in agenda):
        
        agenda [nombre]= telefono
        print("contacto guardado ")
    else: 
        print("el nombre ya se encuentra en la agenda")
        
    respuesta = input ("¿salir? (S/N)")
    if (respuesta == "S") or (respuesta == "s"):
        salir = True
print("mis contactos:", agenda)