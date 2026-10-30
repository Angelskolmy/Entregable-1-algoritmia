
FullParking=[]

class Vehiculo_plaza:  

    def __init__(self, TipoVehiculo=0, TiempoParqueo=0, Factura=0, TarifaParqueo=0, Descuento=0, Matricula=0, Monto=0): 

        self.TipoVehiculo=TipoVehiculo 
        self.TiempoParqueo= TiempoParqueo  
        self.Factura= Factura 
        self.TarifaParqueo= TarifaParqueo  
        self.Descuento= Descuento 
        self.Matricula=Matricula 
        self.Monto= Monto

    def Imprimir_Facturas (self):  

        print(f"-------------Vehiculo tipo {self.TipoVehiculo}-------------\n") 
        print(f"Matricula de vehiculo----------{self.Matricula}\n")
        print(f"Tiempo de uso------------------{self.TiempoParqueo} minutos \n")
        print(f"Cuenta con factura ------------{self.Factura} \n")
        print(f"Tarifa por hora----------------{self.TarifaParqueo}\n")
        print(f"Descuento por factura----------{self.Descuento}\n") 
        print(f"Monto--------------------------{self.Monto}")



    def AfectarVehiculo (self): 

        for Compiler in FullParking: 

            if Compiler.Matricula in FullParking: 

                print(f"Vehiculo con placas {Compiler.Matricula} encontrado") 

                Compiler.Imprimir_Facturas() 

                return Compiler  

            else: 
                print("Vehiculo no encontrado")  

                

    def PreviaIngreso (self): 

        for Nurbulgrim in FullParking: 

            if Nurbulgrim.Matricula in FullParking: 

                print("Datos previamente ingresados") 

                bloqueo= True 

                return bloqueo 

            else: 

                print("Datos nuevos") 

                bloqueo= False 

                return bloqueo

    