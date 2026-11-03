from controladores.ControladorInventario import * 

print("calculadora de parqueadero") 

varinciadora= input("Desa inciar SI NO ").upper()

while varinciadora != "SI" and  varinciadora != "NO":  
    print("opcion invalida") 
    varinciadora= input("Desa inciar SI NO ").upper() 


while varinciadora == "SI":

    print('''

        -1 ingresar datos 
        -2 calcular item 
        -3 listar 
        -4 salir

    ''')
     

    while True: 

        try: 
            opcion= int(input(" ingrese opcion deseada ")) 

        except ValueError:  
            print("opcion invalida")
            continue

        if opcion <= 0 or opcion >4: 
            print("opcion invalida") 
            continue 

        break

    if opcion == 1: 
        IndexItemsForInventori()

    elif opcion == 2:  
        reflejoDeestoItem()

    elif opcion == 3:  
        alllist()

    elif opcion == 4:  
            print("salio del programa")
            break

if varinciadora == "NO":
    print("salio del programa")
