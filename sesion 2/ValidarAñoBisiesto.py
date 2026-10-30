print("calcular año bisiesto") 

BucleAunal= str(input("Iniciar calculo SI NO ")).upper() 

while BucleAunal != "SI" and BucleAunal !="NO": 
    print("opcion invalidad") 
    BucleAunal= str(input("Iniciar calculo SI NO ")).upper()  

while BucleAunal == "SI": 
 

    while True: 

        try:  
            AñoXcotejar= int(input("Ingrese año a calcular ")) 

        except ValueError: 
            print(f"error dato {AñoXcotejar} invalido") 
            continue 

        if AñoXcotejar <= 0 or AñoXcotejar <=1000: 
            print(f"error dato {AñoXcotejar} invalido") 
            continue

        break

    Calcule1= AñoXcotejar % 4 
    Calcule2= AñoXcotejar % 400 
    Calcule3= AñoXcotejar % 100 

    if Calcule1 == 0 or Calcule2 == 0 and Calcule3 >0: 
        print(f"año {AñoXcotejar} es biciesto") 
    else: 
        print(f"Año {AñoXcotejar} no es biciesto")


    BucleAunal= str(input("Iniciar calculo SI NO ")).upper() 

    while BucleAunal != "SI" and BucleAunal !="NO": 
        print("opcion invalidad") 
        BucleAunal= str(input("Iniciar calculo SI NO")).upper()  


print("salio del programa")