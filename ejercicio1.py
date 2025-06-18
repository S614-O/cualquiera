pacientes = {
"H001": ["Laura Pérez", "Pediatría", "11-03-2024"],
"H002": ["Carlos Díaz", "Traumatología", "22-01-2024"],
"H003": ["Daniela Soto", "Neurología", "05-07-2023"],
"H004": ["Matías Rojas", "Pediatría", "14-03-2024"],
"H005": ["Fernanda Silva", "Cardiología", "03-10-2023"],
"H006": ["José Vargas", "Traumatología", "28-03-2024"],
"H007": ["Ana Beltrán", "Neurología", "19-09-2023"],
"H008": ["María Contreras", "Cardiología", "12-01-2024"],
}

while True:
    print("*** MENU HOSPITAL ***")
    print("1.- Pacientes por especialidad")
    print("2.- Porcentaje de ingresos por mes")
    print("3.- Eliminar por paciente ")
    print("4.- Salir")
    
    while True: 
        try:
            op = int(input("Seleccione una opcion (1/4): "))
            break        
        except ValueError:
            print("Error de opcion")
        
    if op == 1:
        print("*** Pacientes por especialidad ***")
        
        especialidad = input("Ingrese la especialidad: ")        
        for i in pacientes.values():
            if i[1].lower() == especialidad.lower():
                print(f"Nombre: {i[0]}")
                
                
    elif op == 2:
        print("*** Porcentaje de ingresados por mes ***")
        
        while True:
            try:
                mes = int(input("Ingrese el mes a consultar como numero: "))
            except ValueError:
                print("El mes debe de ingresar un numero")
            else:
                if mes >= 1 and mes <=12:
                    break
        cont = 0
        for paciente in pacientes.values():
            mes_actual = int(paciente[2].split("-")[1])
            if  mes_actual == mes:
                cont +=1
                
        porc = cont / len(pacientes)*100
        
        print(f"El porcentaje de pacientes del mes {mes} fueron: {porc}")

    elif op == 3:
        print("*** Eliminar Persona ***")
        
        nombre = input("Ingrese el nombre de la persona a eliminar: ")
        
        #codigos = pacientes.keys()
        for codigo in pacientes.keys():
            if pacientes[codigo][0] == nombre: #pacientes[iterador para recorrer la lista][posicion del nombre de la persona a comparar]
                print(f"Se elimino a {nombre}")
                del pacientes[codigo] #Borra del diccionario pacientes que se busca por codigo(iterador para recorrer la lista)
                print(pacientes)
                break
            else:
                print("No se elimino")
        
        
    elif op == 4:
        break
    else:
        print("Ingrese una opcion correcta")
    
    
