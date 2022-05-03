
print("======Cartelera de Cine======")

class Peliculas:
    def __init__(self, titulo, director, genero, duracion):
        self.titulo=titulo
        self.director=director
        self.genero=genero
        self.duracion=duracion 
    
    def agregarCartelera(self): 
            cartelera= open('cartelera.txt','a')
            print("Agregado a la Cartelera")
            print("================")
            cartelera.write('=============''\n')
            cartelera.write('DATOS PELÍCULAS Nº{}:'.format(movie+1)+'\n')
            cartelera.write('Titulo:'+titulo+'\n')
            cartelera.write('Director:'+director+ '\n')
            cartelera.write('genero:'+genero+ '\n')
            cartelera.write('Duración:'+duracion+ '\n')
            cartelera.close()
        
    def imprimirCartelera(self):
            cartelera= open("cartelera.txt")
            print("===Cartelera de la Semana===")
            print(cartelera.read())
            cartelera.close()
            print('==================')

    
for movie in range(5): 
    titulo= input("Ingresar el titulo de la Pelicula nº{}:".format(movie+1))
    director=input("Ingrese  el director de la Pelicula nº{}:".format(movie+1))
    genero=input("Ingrese el genero de la Pelicula nº{}:".format(movie+1))
    duracion= input("Ingrese la duracion de la Pelicula nº{}:".format(movie+1))   
    pelicula=Peliculas(titulo,director, genero, duracion)
    pelicula.agregarCartelera()
pelicula.imprimirCartelera()