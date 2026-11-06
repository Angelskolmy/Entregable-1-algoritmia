from controladores.controladorEstacionamineto import *  

print("calculadora de parqueadero") 

varinciadora= input("Desa inciar SI NO ").upper()

while varinciadora != "SI" and  varinciadora != "NO":  
    print("opcion invalida") 
    varinciadora= input("Desa inciar SI NO ").upper() 


while varinciadora == "SI":

    print('''

        -1 ingresar datos 
        -2 calcular auto 
        -3 listar 
        -4 balance dia 
        -5 salir

    ''')
     

    while True: 

        try: 
            opcion= int(input(" ingrese opcion deseada ")) 

        except ValueError:  
            print("opcion invalida")
            continue

        if opcion <= 0 or opcion >5: 
            print("opcion invalida") 
            continue 

        break

    if opcion == 1: 
        Ingreso_datosParking()

    elif opcion == 2:  
        operaciondatos()

    elif opcion == 3:   
        listar_todo() 

    elif opcion== 4: 
        alquemist()

    elif opcion == 5:  
            print("salio del programa")
            break

if varinciadora == "NO":
    print("salio del programa")
