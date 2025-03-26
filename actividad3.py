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



#CONTRATO DE JORNADA


=>Para el caso de joranada 
  * Se debe solicitar el numero de horas trabajadas y el 
  valor a pagar por hora y el total del salario se calcula de multiplicar 
  el numero de horas por el valor a pagar por hora 
  
#CONTRATO DE PRESTACION DE SERVICIOS

=>Para el caso de prestacion de servicios
 *El valor del contrato 
 *El numero de meses de contrato
 *Antiguedad  del empleado (años)
 El salario neto en este caso se calcula 
   1.Divir el valor de contraro por el numero de meses
   2.Restar el 15% del salario mensual anterior por concepto de eps   
   3.Restar el 10% del salario mensual anterior por concepto de pension
   4.Si el empleado tiene una antiguedad superior a 10 años tendra una
   bonificacion del  0.5% sobre el salario mensual
#CONTRATO TERMINO INDEFINIDO 
=>Para el contrato de termino indefinido se debe solicitar unicamente
la antiguedad en años y el grado o escalafon (1-5)
El salario mensual se calcula de acuerdo a la siguiente tabla de escalafones:
 *Grado 1 : 1.5 Sm
 *Grado 2 : 1.7 Sm
 *Grado 3:  2.0 Sm
 *Grado 4:  2.5 Sm
 *Grado 5:  3.0 Sm
 La bonificacion estara acorde a los siguientes rangos segun la antiguedad:
 * entre 1 y 5 la bonificacion sera del 1%
  entre 6 y 10 años sera del 2%
  Superior a  10 años sera del 3%
  
  Para esos años los descuentos de ley son:
  
  * 25% por concepto de eps
  * 22 % por concepto de pension 
  * 0.1% ARL

"""
#inicializar variables:
#dar vaalor inicial a una variable asi no se utilice en el momento
contrato = input("Ingrese el tipo de contrato (a: indefinido, b: prestación de servicios, c: aprendizaje, d: jornada): ")
salario_neto = 0

# CONTRATO TERMINO INDEFINIDO
if contrato == "a":
    print("Eligió: Contrato a término indefinido")
    antiguedad = int(input("Ingrese la antigüedad en años: "))
    grado = int(input("Ingrese el grado o escalafón (1 - 5): "))
    salario_minimo = int(input("Ingrese el valor del salario mínimo: "))

    salario_mensual = salario_minimo * 1.5

    print("El salario mensual es:", salario_mensual)

    if antiguedad >= 1:
        if antiguedad <= 5:
            bonificacion = salario_mensual * 0.01  
        elif antiguedad <= 10:  
            bonificacion = salario_mensual * 0.02  
        elif antiguedad > 20:
            bonificacion = salario_mensual * 0.03  
        else:
            bonificacion = 0
    else:
        bonificacion = 0

    print("Bonificación por la antigüedad:", bonificacion)

    eps = salario_mensual * 0.20 
    pension = salario_mensual * 0.22  
    arl = salario_mensual * 0.001  

    salario_neto = salario_mensual + bonificacion - eps - pension - arl

    print("El salario neto es:", salario_neto)



# CONTRATO PRESTACION DE SERVICIOS
elif contrato == "b":
    print("Eligió: Contrato por prestación de servicios")
    valor_contrato = int(input("Ingrese valor del contrato: "))
    numero_meses = int(input("Ingrese el número de meses del contrato: "))
    antiguedad = int(input("Ingrese el número de años del contrato: "))

    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension
    
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion

    print("El salario neto es:", salario_neto)


# CONTRATO DE APRENDIZAJE
elif contrato == "c":
    print("Eligió: Contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el valor del salario mínimo: "))
    salario_neto = salario_minimo - (salario_minimo * 0.25)  # Se calcula el 25% de descuento
    print("El salario neto es:", salario_neto)


# CONTRATO POR JORNADA
elif contrato == "d":
    print("Eligió: Contrato por jornada")
    numero_horas = int(input("Ingrese el número de horas: "))
    valor_hora = int(input("Ingrese el valor por hora: "))
    salario_neto = numero_horas * valor_hora
    print("El salario neto es:", salario_neto)

else:
    print("Tipo de contrato no existente")

print("Fin del programa")
