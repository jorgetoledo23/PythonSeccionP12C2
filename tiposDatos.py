# int -> Integer = Entero  <class 'int'>
edad = 10
print(type(edad))
precio = 99990
cantHijos = 2
cantProductos = 10

#edad = int(input("Ingrese su Edad: "))
#print(type(edad))

#if edad >= 18:
    #print("Mayor de Edad")


#String -> cadena de texto / literal <class 'str'>
nombre = "Jorge Toledo"
print(type(nombre))
print(nombre)
apellido = "Toledo"
direccion = "Merced 750 Curico"
telefono = "+569 1234 1234"
producto = "Logitech G502 Wireless"

#float -> Float - Numeros de Punto Flotante (Decimal) <class 'float'>
vDolar = 1.11111111111111111111
PI = 3.1416
GRAVEDAD = 9.13
radioCirculo = 4.15
print(type(vDolar))


#ValueError
#edad = int(input("Ingrese su Edad: "))
#print(type(edad))


PI = 3.1416
Pi = int(PI)
print(type(Pi))
print(Pi)

division = 10 / 3
print(int(division))

edad = 20
edad2 = float(edad)
print(edad2)


#Boolean -> Solo puede tomar valor Verdadero o Falso <class 'bool'>
semaforo = True
print(type(semaforo))
semaforo = False
print(type(semaforo))

#0 = Falso, 1 = Verdadero
semaforo = "Hola"

#semaforo == True:
if semaforo:
    print("Semaforo esta en Verdadero")
else:
    print("Semaforo esta en Falso")


#int, str, float, bool

edad = False
while not(edad):
    try:
        edad = int(input("Ingrese su Edad: "))
        break
    except:
        print("El Dato ingresado NO corresponde a una Edad VALIDA!")
print("Dato ingresado con Exito!")




