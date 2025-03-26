"""
ACTIVIDAD:3
Elabore un programa que permita calcular el salario neto de un 
empleado despues de descontar los descuentos por conceptos de 
salud, pension, ARL

1.El programa debe solicitar el tipo de empleado:
   a.Contrato a termino indefinido
   b.Contrato por presentacion de servicios 
   c.Contrato de aprendizaje 
   d.Contrato por jornada (freelance)

=>Para el caso de joranada 
  * Se debe solicitar el numero de horas trabajadas y el 
  valor a pagar por hora y el total del salario se calcula de multiplicar 
  el numero de horas por el valor a pagar por hora 


"""

contrato = input("Ingrese el tipo de contrato: ")
salario_neto= 0 


#CONTRATO DE TERMINO INDEFINIDO 

if contrato == "a":
 print("Eligio contrato a termino indefinido")
 
 #CONTRATO DE PRESTACION DE SERVICIOS

elif contrato == "b":
 print("Eligio contrato por presentacion de servicios ")
 
 #CONTRATO DE APRENDIZAJE

elif contrato == "c":
 print("Eligio contrato de aprendizaje ")
 salario_minimo =int(input("Ingerese el valor del salario minimo"))
 salario_neto = salario_minimo - (salario_minimo * (0.25))
 print ("El salario neto es ", salario_neto)

 
 
 


#CONTRATO DE JORNADA

elif contrato == "d":
 print("Eligio contrato por jornada (freelance) ")
 #inicializar variables
 #dar valor inicial a una variable
 #asi no se utilice en el momento 
 
 #Variable local:
 #Vaiable que solo se puede utilizar en un bloque por lo tanto solo pertenece a ese 
 
 numero_horas = int(input("Ingrese numero de horas"))
 valor_hora = int(input("Ingrese valor de hora apagar"))
 salario_neto = numero_horas * valor_hora
 print ("El salario neto es ", salario_neto)

else:
 print ("El tipo de contrato no existe ")
print("Fin del programa")


