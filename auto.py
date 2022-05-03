print('=====INVENTARIO AUTOMOVILES=====')

class Automovil:
    def __init__(self, color,marca,modelo, puertas , patente) :
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.puertas= puertas
        self.patente=patente


    def agregarInventario(self):
            inventario= open('Inventario.txt','a')
            print("Agregado al inventario")
            print("================")
            inventario.write('=============''\n')
            inventario.write('DATOS AUTOS Nº{}:'.format(auto+1)+'\n')
            inventario.write('Marca:'+marca+'\n')
            inventario.write('Modelo:'+modelo+ '\n')
            inventario.write('Color:'+color+ '\n')
            inventario.write('Puertas:'+puertas+ '\n')
            inventario.write('Patente:'+patente+ '\n')
            inventario.close()
    
    def imprimirBasedatos(self):
            inventario= open("Inventario.txt")
            print("==Inventario Autos ==")
            print (inventario.read())
            inventario.close()
        
        
        
for auto in range(5): 
    color= input("Ingresar color del auto nº{}:".format(auto+1))
    marca=input("Ingrese la marca del auto nº{}:".format(auto+1))
    modelo=input("Ingrese el modelo del auto nº{}:".format(auto+1))
    puertas= input("Ingrese en numero de puertas del auto nº{}:".format(auto+1))  
    patente= input("Ingrese la patente del auto nº{}:".format(auto+1))
    automovil=Automovil(color,marca,modelo,puertas,patente)
    automovil.agregarInventario()
automovil.imprimirBasedatos()   
    
    