
estrato = int(input("Ingresa el estrato (1/2): "))
edad = int(input("Ingresa tu edad: "))
matricula =float(input("Ingresa el valor de la matrícula: "))

if estrato == 1:
    if edad < 18:
        descuento = matricula * 0.20
    else:
        descuento = matricula * 0.15
elif estrato == 2:
    if edad < 18:
        descuento = matricula * 0.10
    else:
        descuento = matricula * 0.05

precio= matricula - descuento

print(f"El descuento es: {descuento}")
print(f"El precio a pagar por la matrícula es: {precio}")
print("Fin del programa")
