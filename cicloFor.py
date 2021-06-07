for i in range(6):
    print(i)

for i in range(1, 6):
    print(i)

#C -> Comienzo | L -> Limite (Hasta Donde) | A -> Aumento
#              C  L  A
for i in range(1, 6, 2):
    print(i)

listFrutas = ["Manzana", "Pera", "Cereza"]
for fruta in listFrutas:
    print(fruta)


listAutos = ["Audi", "Mazda", "Honda"]
for a in listAutos:
    if a == "Audi":
        print("Es Aleman")
    if a == "Mazda":
        print("Es Japones")
    if a == "Honda":
        print("Es Japones")

marcaBuascada = input("Ingrese una marca de Vehiculo: ")
encontrado = False
listAutos = ["Audi", "Mazda", "Honda"]
for a in listAutos:
    if a == marcaBuascada:
        encontrado = True
        break
if encontrado:
    print("La marca se encontro en el listado")
else:
    print("La marca NO se encuentra en el listado")