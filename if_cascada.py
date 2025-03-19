"""
#IF EN CASCADA

Es una estructura selectiva compuesta por multiples 
condicionales seguidos unos de otros 

if condicional1:
    Instruccion1
    Instruccion2 

elif condicional2: 
    Instruccion3
    Instruccion4
    
elif condicional3: 
    Instruccion5
    Instruccion6
    
    NOTA: cada condicional es mutuamente excluyente en si solo se puede ejecutar 
    un caso no se pueden ejecutar  al mismo tiempo
"""
#Ejemplo 
#Vamos a hacer un pequeño traductor 
#El programa debe permitir leer por teclado una fruta en español 
#y debe mostrar esa fruta en ingles 

fruta_es= input("Ingresa La Fruta:")
if fruta_es== "manzana" or fruta_es  =="manzana":
    print("apple")
elif fruta_es =="naranja" or fruta_es =="naranja"  :
    print("orange")
elif fruta_es =="uvas" or fruta_es == "uva" :
    print("grape")
    
#caso por defecto
#default 
else:
    print ("No se encontro traduccion")
    
    