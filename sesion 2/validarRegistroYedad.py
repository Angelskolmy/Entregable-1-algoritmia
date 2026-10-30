print("Welcome to Afterlife Punk!!") 

varbuclePrinp= input("Deseas registrarte en el var SI o NO ").upper() 

while varbuclePrinp != "SI" and varbuclePrinp!= "NO": 

    print(f"repsuesta {varbuclePrinp} invalidad punk SI o NO") 
    varbuclePrinp= input("Deseas registrarte en el var SI o NO ").upper() 

while varbuclePrinp == "SI":

    Terminos= str(input("Este var es una subdivision de arasaka Acepta el NDA SI - NO ")).upper() 

    while Terminos != "SI" and Terminos != "NO": 
        print("Acepta los terminos o largate punk") 
        Terminos= str(input("Este var es una subdivision de arasaka Acepta el NDA SI - NO ")).upper()    

    if Terminos == "NO": 
        break

    while True:
        try: 
            Edad_Egerunner= int(input("Cual es tu edad punk "))          
        except ValueError:
            print(f" sabes contar punk?") 
            continue 

        if Edad_Egerunner <=0 or Edad_Egerunner >101: 
            print(f"No me mientas punk no puedes tener {Edad_Egerunner} años") 
            continue 

        break


    if Terminos == "SI" and Edad_Egerunner >=15: 
        print("Bienvenido al afterlife tomate un rebeca red la casa invita") 

    else: 
        print("Largate punk MaxStack biene en camino") 

    varbuclePrinp= input("Deseas registrarte en el var SI o NO ").upper() 

    while varbuclePrinp != "SI" and varbuclePrinp!= "NO": 

        print(f"repsuesta {varbuclePrinp} invalidad punk SI o NO") 
        varbuclePrinp= input("Deseas registrarte en el var SI o NO ").upper() 

print("Largate punk!!")
