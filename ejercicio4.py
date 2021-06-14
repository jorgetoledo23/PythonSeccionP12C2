#Ingresar una marca de auto a traves de INPUT, buscarla en el listado y retornar
#"Encontrado" si existe o "NO Encontrado" si no existe la marca dentro del listado

marcaBuscada = input("Ingrese su Marca de Vehiculo: ")
listAutos = ["Audi", "Mazda", "Honda", "Mercedez Benz", "KIA", "FIAT"]
encontrado = False

for auto in listAutos:
    if marcaBuscada == auto:
        encontrado = True
        break
#if encontrado == True:
if encontrado:
    print("Auto Encontrado")
else:
    print("Auto NO Encontrado")


#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
#Si trabaja 40 horas o menos se le paga $1600 por hora
#Si trabaja más de 40 horas se le paga $1600 por cada una de las primeras 40 horas 
# y $2000 por cada hora extra.


#Crear un algoritmo que permita leer n números y determinar cuál fue el mayor 
#ingresado y, cuál el menor.