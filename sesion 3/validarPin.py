
print("validar pin 6 digitos 3 intentos")  

cont=0
pasword= "234812"


for x in range(0,3,1): 

    cont+=1 

    while True: 
        try: 
            pin= str(input("ingrese su pin ")) 

        except ValueError: 
            print("solo numeros enteros") 
            continue

        if len(pin) !=6 or not pin.isalnum(): 
            print("maximo 6 digitos sin caracteres especiales")  
            continue 

        break     

    if pin == pasword: 
        pin = pasword 
        print("contraseña correcta iniciando sesion")   
        break

    if cont == 3:

        pin="Bloqueada" 
        print(f"sobre paso limite de intentos cuenta {pin}")