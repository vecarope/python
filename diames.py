
mes =['Enero','Febrero','Marzo','Abril','Mayo', 
        'Junio', 'Julio', 'Agosto', 'Septiembre', 
        'Octubre', 'Noviembre','Diciembre']

print("¿cuantos días tiene cada mes?")

while True:
    def dia_meses(mes):
        n_mes=int(input("ingrese el numero del mes:"))
        if n_mes < 1 or n_mes > 12:
                print("Ingrese un mes entre 1 al 12") 
        elif n_mes in [4, 6, 9, 11]:
                print(mes[n_mes-1],"tiene 30 días")
        else:
            if n_mes == 2: 
                print(mes[n_mes-1], "tiene 28 días")
            else:
                print(mes[n_mes-1],"tiene 31 días") 
    dia_meses(mes)