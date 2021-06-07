#Dentro de un grupo de alumnos determinar Promedio de Edad de Hombres, Mujeres y de todo el grupo

promedioHombres = 0
promedioMujeres = 0
promedioGeneral = 0

sumaMujeres = 0
sumaHombres = 0

contadorMujeres = 0
contadorHombres = 0

cantidadAlumnos = int(input("Ingresa cantidad de Alumnos: "))

for i in range(1, cantidadAlumnos + 1):
    edad = int(input(f"Ingresa la Edad del Alumno {i}: "))
    genero = input("Es Hombre o Mujer: ")
    if genero == "Mujer":
        sumaMujeres += edad
        contadorMujeres += 1
    if genero == "Hombre":
        sumaHombres += edad
        contadorHombres += 1

promedioHombres = sumaHombres / contadorHombres
promedioMujeres = sumaMujeres / contadorMujeres
promedioGeneral = (sumaMujeres + sumaMujeres) / (contadorHombres + contadorMujeres)

print(f"El Promedio de Edad de Mujeres es {promedioMujeres}")
print(f"El Promedio de Edad de Hombres es {promedioHombres}")
print(f"El Promedio de Edad General es {promedioGeneral}")