
FullParking=[]

class Vehiculo_plaza:  

    def __init__(self, TipoVehiculo=0, TiempoParqueo=0, Factura=0, TarifaParqueo=0, Matricula=0, Monto=0): 

        self.TipoVehiculo=TipoVehiculo 
        self.TiempoParqueo= TiempoParqueo  
        self.Factura= Factura 
        self.TarifaParqueo= TarifaParqueo  
        self.Matricula=Matricula 
        self.Monto= Monto

    def Imprimir_Facturas (self):  

        print(f"-------------Vehiculo tipo {self.TipoVehiculo}-------------\n") 
        print(f"Matricula de vehiculo----------{self.Matricula}\n")
        print(f"Tiempo de uso------------------{self.TiempoParqueo} minutos \n")
        print(f"Cuenta con factura ------------{self.Factura} \n")
        print(f"Tarifa por hora----------------{self.TarifaParqueo}\n")
        print(f"Monto--------------------------{self.Monto} \n \n")



    def AfectarVehiculo (self): 

        for Compiler in FullParking: 

            if Compiler.Matricula == self.Matricula: 

                print(f"Vehiculo con placas {Compiler.Matricula} encontrado") 

                Compiler.Imprimir_Facturas() 

                return Compiler  

        print("Vehiculo no encontrado")   
        return None

                

    def PreviaIngreso (self): 

        for Nurbulgrim in FullParking: 

            if Nurbulgrim.Matricula == self.Matricula: 

                bloqueo= True 

                return bloqueo 

        print("Datos nuevos") 

        bloqueo= False 

        return bloqueo 

    def Changelogvehicle (self, newMonto): 

        for Hellhound in FullParking: 

            if Hellhound.Matricula == self.Matricula: 

                Hellhound.Monto = newMonto 

                return 
            

def listar_todo ():  

    tamaño=len(FullParking)

    if tamaño>0 : 
        for rakuten in FullParking: 
            rakuten.Imprimir_Facturas() 
    else: 
        print("lista vacia/no data")


def Ingreso_datosParking(): 

    while True : 

        try: 
            CantidadRegistros= int (input("Cantidad de Registros a ingresar ")) 
            
        except ValueError: 
            print(f"dato invalido solo numeros enteros") 
            continue 

        if CantidadRegistros <= 0: 
            print(f"no se puede iingresar un valor negativo o nulo") 
            continue 

        break 

    for CipherBucle in range(0 , CantidadRegistros, 1):  
        
        print("verificacion de plaza")  

        while True:

            matriculaVerfiy= input("ingrese la matricula del auto a registrar ") 
            
            while len(matriculaVerfiy)<=0 or len(matriculaVerfiy)>6  or not matriculaVerfiy.isalnum(): 
                print(f"matricula invalida {matriculaVerfiy}, max 6 caracteres y numeros sin simbolos")

                matriculaVerfiy= input("ingrese su mnatricula ") 

            objVerify= Vehiculo_plaza(Matricula= matriculaVerfiy ) 
            NotDuplicate= objVerify.PreviaIngreso()

            if NotDuplicate == True: 

                print(" vehiculo ya existente \n Vehiculo no sera ingresado ")  
                continue 

            else: 
                print(" vehiculo nuevo ingreso permitido ")
                break

        
        TypeVehicule= str (input("Es CARRO o MOTO ")).upper() 

        while TypeVehicule != "CARRO" and TypeVehicule !="MOTO": 
            print("Error, Posibles opciones CARRO o MOTO") 
            TypeVehicule= str (input("Es CARRO o MOTO ")).upper()   

        while True: 

            try:  
                TiempoUsoPark= int(input("Cuanto tiempo uso el parking en minutos ")) 

            except ValueError: 
                print("solo numeros enteros y no negativos")
                continue 

            if TiempoUsoPark <=0 or TiempoUsoPark >600: 
                print(f"error de ingreso en {TiempoUsoPark} cantidad minima de 1 minuto maxima de 600 minutos") 
                continue 

            break  

        TipoTarifa=0 

        if TiempoUsoPark >=60: 
            TipoTarifa= 4000 

        if TiempoUsoPark<60: 
            TipoTarifa=2000 

        if TiempoUsoPark <=15: 
            TipoTarifa=0
             

        FacturaComercial= input("Tiene factura del centro comercial SI o NO ").upper()
        while FacturaComercial !="SI" and FacturaComercial !="NO": 
            print("error, opcion invalida") 
            FacturaComercial= input("Tiene factura del centro comercial SI o NO ").upper()
            
        IdMatricula= input("ingrese su matricula ") 

        while len(IdMatricula)<=0 or len(IdMatricula)>6  or not IdMatricula.isalnum(): 
            print(f"error matricula invalida {IdMatricula}, maximo 6 caracteres y numeros sin simbolos")
            IdMatricula= input("ingrese su matricula ") 

        IteracionVehiculo= Vehiculo_plaza(
            TipoVehiculo= TypeVehicule, 
            TiempoParqueo= TiempoUsoPark, 
            Factura= FacturaComercial, 
            TarifaParqueo= TipoTarifa, 
            Matricula= IdMatricula,
        )  

        FullParking.append(IteracionVehiculo)  

        print("Vehiculo guardado correctamente")

def operaciondatos (): 

    VehiculoId= input("escriba la matricula del vehiculo ") 

    while len(VehiculoId)<=0 or len(VehiculoId)>6  or not VehiculoId.isalnum(): 
        print(f" Matricula invalida \n maximo 6 Caracteres \n sin simbolos especiales ni espacios ")  
        VehiculoId= input("escriba la matricula del vehiculo ")  

    Expediente= Vehiculo_plaza(Matricula=VehiculoId)   
    halor= Expediente.PreviaIngreso()
    Ralor= Expediente.AfectarVehiculo()    

    if halor == True :  

        absoluteDivisor= Ralor.TiempoParqueo / 60 

        if absoluteDivisor <= 0.25:  

            print("uso gratuito de parkin los priomeros 15 minutos") 

            Ralor.Imprimir_Facturas()

        elif absoluteDivisor> 0.25 and absoluteDivisor<1:  

            if Ralor.Factura == "SI": 
                
                print("cuenta con un 50 porciento de descunto por tener un afactuira del centro comercial \n")  

                New_Monto= Ralor.TarifaParqueo*0.50 

                Ralor.Changelogvehicle(New_Monto)

                Ralor.Imprimir_Facturas() 

            else:  
                tartaro= Ralor.TarifaParqueo
                print(f"cobro por fraccion {Ralor.TarifaParqueo} por tiempo menor a 1 hora\n") 
                Ralor.Changelogvehicle(tartaro)
                Ralor.Imprimir_Facturas()



        elif absoluteDivisor >= 1:

            if Ralor.Factura == "SI":   

                print("cuenta con un 50 porciento de descunto por tener un afactuira del centro comercial \n")

                Pyament= (Ralor.TiempoParqueo / 60)%1 

                if Pyament >0: 

                   Aritmic= ( int(absoluteDivisor)+ 1) * Ralor.TarifaParqueo   
                   New_Monto= Aritmic * 0.50 
                   if New_Monto >30000: 
                       print(f"cobro {New_Monto} supero maximo por dia de 30000")
                       New_Monto=30000
                   Ralor.Changelogvehicle(New_Monto) 
                   Ralor.Imprimir_Facturas()

                else: 
                    Aritmic2= absoluteDivisor * Ralor.TarifaParqueo  
                    New_Monto2=Aritmic2*0.50 
                    if New_Monto2 >30000: 
                        print(f"cobro {New_Monto2} supero maximo por dia de 30000")
                        New_Monto2=30000
                    Ralor.Changelogvehicle(New_Monto2) 
                    Ralor.Imprimir_Facturas()


            else: 

                Pymaent2= (Ralor.TiempoParqueo / 60)%1

                if Pymaent2>0:  
                    Aritmic33= (int(absoluteDivisor) + 1) * Ralor.TarifaParqueo  
                    if Aritmic33 >30000: 
                        print(f"cobro {Aritmic33} supero maximo por dia de 30000") 
                        Aritmic33=30000 
                    Ralor.Changelogvehicle(Aritmic33) 
                    Ralor.Imprimir_Facturas() 

                else: 
                    Aritmic34= absoluteDivisor * Ralor.TarifaParqueo
                    if Aritmic34 >30000: 
                        print(f"cobro {Aritmic34} supero maximo por dia de 30000") 
                        Aritmic34=30000 
                    Ralor.Changelogvehicle(Aritmic34) 
                    Ralor.Imprimir_Facturas() 
        
    else:  
        print("vehiculo inexistente")
        return 
    



    


