Algoritmo CalculadoraPromedio
	
	Escribir "Desea iniciar claculo SI NO" 
	Definir OpBuclePrinp Como Caracter; 
	Leer OpBuclePrinp; 
	
	Mientras  OpBuclePrinp <> "SI" y OpBuclePrinp <> "NO" Hacer;
		Escribir "Opcion invalida seleccione SI o NO"; 
		Leer OpBuclePrinp;
	FinMientras;
		
	
	Mientras OpBuclePrinp == "SI" Hacer;
			
		Definir cantidadPonderar Como Entero;  
		Escribir "numero de notas a ponderar"; 
		Leer cantidadPonderar;  
		
		Mientras cantidadPonderar <0 Hacer
			Escribir "no se puedem ingresar numeros negativos"; 
			Leer cantidadPonderar; 
		FinMientras
		
		Definir ArchNotas Como Entero; 
		Dimensionar ArchNotas[cantidadPonderar];  
		
		
		Para bucleclaculator <- 1 Hasta cantidadPonderar Hacer
			Escribir "Ingrese nota numero ", bucleclaculator
			Leer ArchNotas[bucleclaculator]
			
			Mientras ArchNotas[bucleclaculator] < 0 Hacer
				Escribir "No se puede ingresar una nota negativa"
				Leer ArchNotas[bucleclaculator]
			FinMientras
		FinPara
		
		Definir total1 Como Entero;
		total1<-0
		
		Para Sumador <- 1 hasta cantidadPonderar Hacer;  
			
			total1<- total1 + ArchNotas[cantidadPonderar];
			
			
		FinPara 
		
		Definir Resultado Como Entero; 
		
		Resultado<- total1/cantidadPonderar; 
		
		Escribir "el promedio es de ", Resultado;
		
		
		Escribir "desea volver a operar ? seleccione SI o NO"; 
		Leer OpBuclePrinp;  
		
		Mientras  OpBuclePrinp <> "SI" y OpBuclePrinp <> "NO" Hacer;
			Escribir "Opcion invalida seleccione SI o NO"; 
			Leer OpBuclePrinp;
		FinMientras;
		
	FinMientras; 
	
	Escribir "Salio de la calculadora";
		
	
FinAlgoritmo
