Algoritmo CalculadoraCuentas  
	
	Escribir "quiere iniciar programa SI o NO" 
	Definir OpcionBucle Como Caracter; 
	Leer OpcionBucle;
	
	Mientras OpcionBucle == "SI" Hacer
		
		Escribir "Escriba monto total de la cuenta";
		Definir Monto_General Como Real; 
		Leer Monto_General;   
		
		Mientras  Monto_General < 0 Hacer
			Escribir "no se admiten montos negativos"; 
			Leer Monto_General
		FinMientras;
		
		
		Escribir "Escriba el porcentaje de propina sin simbolo"; 
		Definir  PercentProp Como Real; 
		Leer  PercentProp;  
		
		Mientras  PercentProp < 0 Hacer
			Escribir "no se admiten porcentajes negativos"; 
			Leer PercentProp
		FinMientras;
		
		
		Escribir "Cantidad de personas a dividir cuenta"; 
		Definir  CantPersonsCount Como Real; 
		Leer CantPersonsCount; 
		
		
		Mientras  CantPersonsCount < 1 Hacer
			Escribir "tiene que haber mas de 1 persona"; 
			Leer CantPersonsCount
		FinMientras;
		
		
		Definir MontoReal Como Real; 
		MontoReal <- Monto_General+(Monto_General*(PercentProp/100));
		
		Definir PrecioXcabeza Como Real; 
		PrecioXcabeza <- MontoReal/CantPersonsCount; 
		
		Escribir "Cuenta de ", Monto_General, " con propina del ","% ",PercentProp," queda en ",PrecioXcabeza," por persona";	 
		
		Escribir "quiere continuar programa SI o NO" 
		Leer OpcionBucle;
		
	FinMientras; 
	
	Escribir "Fin algoritmo"

FinAlgoritmo
