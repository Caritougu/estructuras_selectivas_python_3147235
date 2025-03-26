"""
If Aninados
if dentro de otros if 

Sintax:
if condicion:
   if condicion:
     print("mensaje")
   else:
     print("mensaje)

No confundir con elif (if en cascada)

"""

#Ejemplo 1:

#Modifique el ejercicio de la edad 
#para las siguientes condiciones 
#Si es mayor de 18 años 
#pero no tiene documento no puede votar 
#de lo contrario si puede votar 
#Condicion 2 : Si es menor de 18 años 
#no puede votar
#utilice estrcutura de if anidados

edad = int(input("iNGRESE SU EDAD"))
if edad >= 18:
  documento = input("Tiene documento? (si/no):") 
  if documento =="si": 
     print ("Puede votar")
  else:
     print ("No puede votar")
else:
    print("No puede votar")   