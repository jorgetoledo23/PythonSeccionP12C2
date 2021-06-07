#Leer un numero x y responder si es par o impar

numero = int(input("Ingrese un Numero cualquiera: "))

restoDivision = numero % 2 # 11 / 2 = 5     10 % 2 = 1

if restoDivision == 0:
    #numero es PAR
    print("El numero ingreso es un numero PAR")
else:
    #numero es IMPAR
    print("El numero ingreso es un numero IMPAR")