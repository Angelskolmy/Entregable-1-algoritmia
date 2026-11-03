FullInventario=[] 

class Item_Inventario: 

    def __init__(self, Nombreitem=0, IdItem=0, CantStock=0, EstadoColor=0): 

        self.Nombreitem=Nombreitem 
        self.IdItem= IdItem 
        self.CantStock=CantStock 
        self.EstadoColor=EstadoColor

    def imprimir_stockItem(self): 

        print(f"------------articulo con id {self.IdItem}----------------\n")
        print(f"----- articulo: {self.Nombreitem}\n")
        print(f"----- stock actual: {self.CantStock}\n")
        print(f"----- color de stock: {self.EstadoColor}\n") 
        print(f"\n")


    def ControlPass (self): 

        for haxorus in FullInventario: 

            if haxorus.IdItem == self.IdItem:

                varblock= True 
                return varblock 

        varblock=False 
        return varblock 
    

    def Vectoritem (self): 

        for Tyrant in FullInventario: 

            if Tyrant.IdItem == self.IdItem: 

                print(f"item encontrado \n") 
                Tyrant.imprimir_stockItem() 

                return Tyrant 

        print("item inexistente")
        Tyrant= None 
        return Tyrant 


    def updateItem (self, changerItem1, changerItem2): 

        for Leaker in FullInventario: 

            if Leaker.IdItem == self.IdItem: 

                Leaker.CantStock = changerItem1  
                Leaker.EstadoColor = changerItem2
                return 


def alllist(): 

    longitud= len(FullInventario)  

    if longitud > 0: 

        for rakan in FullInventario:  

            print("lista actual")

            rakan.imprimir_stockItem()  
    else: 
        print("lsita vacia no se puede imprimir")

            

def IndexItemsForInventori (): 


    while True: 

        try:  
            CabtidadIngresos= int(input("cantidad de itemas a ingresar "))  

        except ValueError: 
            print(f"ingreso invalido solo se permiten numeros") 
            continue

        if CabtidadIngresos <= 0 : 
            print(f"ingreso {CabtidadIngresos} invalido  solo numeros positivos mayores a 0") 
            continue 

        break 

    for aqularre in range(0, CabtidadIngresos, 1):  

        while True : 

            serialitem= str(input("ingrese un codigo de maximo 6 caracteres ")) 

            while len(serialitem)<=0 or len(serialitem)>6 or not serialitem.isalnum(): 
                print(f"ingreso {serialitem} invalido maximo 6 caracteres sin simbolo especiales ni espacios solo letros y numeros") 
                serialitem= str(input("ingrese un codigo de maximo 6 caracteres "))  

            VerifyIdItem= Item_Inventario(IdItem= serialitem) 
            tarlty=VerifyIdItem.ControlPass() 

            if tarlty == True: 

                print(f"item con id {serialitem} encontrado, ingreso invalido, ingreso duplicado")  
                continue 

            else: 
                print(f"datos no encontrados, registro permitido") 
                break 

        NombreItem= str(input("ingrese Nombre del item maximo 60 caracteres ")) 

        while  len(NombreItem)<=0 or len(NombreItem)>60: 
            print(f"nombre {NombreItem} execido la cantidad limite de caracteres ") 
            NombreItem= str(input("ingrese Nombre del item maximo 60 caracteres "))  


        while True: 

            try: 

                CantProducto= int(input("ingrese la cantidad del producto "))

            except ValueError:  
                print(f"ingreso invalido solo cantidades positivas de numeros enteros") 
                continue

            if CantProducto <0: 
                print(f"ingreso {CantProducto} invalido solo cantidades positivas de numeros enteros") 
                continue 

            break 

        if CantProducto == 0: 

            StateColor= "ROJO" 

        if CantProducto>0 and CantProducto<10: 

            StateColor= "AMARILLO" 

        if CantProducto>=10: 

            StateColor="VERDE" 

        IterObject= Item_Inventario(Nombreitem=NombreItem,  IdItem=serialitem,  CantStock=CantProducto, EstadoColor=StateColor) 
        FullInventario.append(IterObject) 

        print("item correctamente ingresado")


def reflejoDeestoItem():   

    identificadorClave= input("ingrese un codigo de maximo 6 caracteres ") 

    while len(identificadorClave)<=0 or len(identificadorClave)>6 or not identificadorClave.isalnum(): 
        print(f"ingreso {identificadorClave} invalido maximo 6 caracteres sin simbolo especiales ni espacios solo letros y numeros") 

        identificadorClave= input("ingrese un codigo de maximo 6 caracteres ") 

    regulusEstado= Item_Inventario(IdItem=identificadorClave) 
    Descartes=regulusEstado.ControlPass()  
    Arcax= regulusEstado.Vectoritem()

    if Descartes == True: 

        if Arcax.EstadoColor == "ROJO":  

            print("fuera de stock no hay existencias de este producto\n se necesitan cambios\n")    

            Cambiovar= input("desea hacer cambios en cantidad SI o NO ").upper() 

            while Cambiovar != "SI" and Cambiovar != "NO": 
                print("opcion invalida") 
                Cambiovar= input("desea hacer cambios en cantidad SI o NO ").upper()  

            if Cambiovar == "SI": 

                while True: 
                
                    try: 
                        CantProducto= int(input("ingrese la cantidad del producto "))
        
                    except ValueError:  
                        print(f"ingreso invalido solo cantidades positivas de numeros enteros") 
                        continue
        
                    if CantProducto <0: 
                        print(f"ingreso {CantProducto} invalido solo cantidades positivas de numeros enteros") 
                        continue 
        
                    break  

                if CantProducto == 0: 
                
                    StateColor= "ROJO" 
        
                if CantProducto>0 and CantProducto<10: 
        
                    StateColor= "AMARILLO" 
        
                if CantProducto>=10: 
        
                    StateColor="VERDE"  

                Arcax.updateItem(CantProducto, StateColor) 

                print("cambios ejecutados \n")  

                Arcax.imprimir_stockItem() 

            else: 
                print("producto actual sin cambios\n") 
                Arcax.imprimir_stockItem()



           

        elif Arcax.EstadoColor == "AMARILLO":  

            print(" existencias de item cerca de terminarse  \n")  

            Cambiovar= input("desea hacer cambios en cantidad SI o NO ").upper() 

            while Cambiovar != "SI" and Cambiovar != "NO": 
                print("opcion invalida") 
                Cambiovar= input("desea hacer cambios en cantidad SI o NO ").upper()  

            if Cambiovar == "SI": 

                while True: 
                
                    try: 
                        CantProducto= int(input("ingrese la cantidad del producto "))
        
                    except ValueError:  
                        print(f"ingreso invalido solo cantidades positivas de numeros enteros") 
                        continue
        
                    if CantProducto <0: 
                        print(f"ingreso {CantProducto} invalido solo cantidades positivas de numeros enteros") 
                        continue 
        
                    break   

                newCantidad= Arcax.CantStock + CantProducto  

                if newCantidad == 0: 
                                
                    StateColor= "ROJO" 

                if newCantidad>0 and CantProducto<10: 

                    StateColor= "AMARILLO" 

                if newCantidad>=10: 

                    StateColor="VERDE"   

                Arcax.updateItem(newCantidad, StateColor) 
                
                print("cambios ejecutados \n")  

                Arcax.imprimir_stockItem() 


            else: 
                print("producto actual sin cambios \n") 
                Arcax.imprimir_stockItem()



        elif Arcax.EstadoColor == "VERDE": 

            print(f"estok en buena cantidad \n no se precisan cambios \n") 

            Arcax.imprimir_stockItem()

    else: 
        print("item no encontrado")
        return



            
