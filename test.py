edad = False
while not(edad):
    try:
        edad = int(input("Ingrese su Edad: "))
    except:
        print("El Dato ingresado NO corresponde a una Edad VALIDA!")
print("Dato ingresado con Exito!")