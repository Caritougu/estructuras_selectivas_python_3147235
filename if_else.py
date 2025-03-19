"""
If else:

Sirve  para determinar dos caminos de ejecucion 
basados en la evaluacion de una condicional. 

if condicional:
    Instruccion1
    Instruccion2 

else: 
    Instruccion3
    Instruccion4



"""

#Ejemplo
#Elabore un programa en python que determine si una persona 
# es mayor o menor de edad y por tanto, habilitala para votar

edad= int (input("Ingrese su edad"))
documento= input("Tiene documento (SI/NO):")
if edad >=18 and documento == "SI":
  print ("Usted es mayor de edad ")  
  print ("Puede votar")  
else:
  print ("Usted es menor de edad ")  
  print("O")
  print ("No puede votar ")  
print("Fin del programa")