varbucled=input("generar piramide si o no").upper() 

while varbucled == "SI":

    while True: 

        try: 
            numeroFilas= int(input("cuantas filas tendra la piramide ")) 
        except ValueError: 
            print("solo numeros") 
            continue

        if numeroFilas<=0 or numeroFilas>100: 
            print("solo mayores a 0") 
            continue 

        break

    realbuclador= numeroFilas+1

    for x in range(1,realbuclador,+1):  

        varasterisco= (x * 2) - 1

        Espacios= numeroFilas - x

        strasteriscos= "*"*varasterisco
        Espacios2= " " * Espacios

        print(Espacios2,strasteriscos)  

print("salio dl programa") 



    


    
    