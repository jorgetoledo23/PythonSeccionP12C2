#Determinar si una persona es Mayor o Menor de Edad

edad = 70

if edad >= 18:
    print("Es Mayor")
else:
    print("Es Menor")

#Determinar si una persona es Mayor o Menor de Edad o Adulto Mayor
#Menor 0 - 18
#Mayor 18 - 65
#Adulto Mayor 66+
if edad < 18:
    print("Es Menor")
else:
    if edad < 66:
        print("Es Mayor")
    else:
        print("Es Adulto Mayor")

if edad < 18:
    print("Es Menor")
elif edad < 66:
    print("Es Mayor")
else:
    print("Es Adulto Mayor")


#and, or, not
nacionalidad = "chileno"
edad = 25
sueldo = 350000

if nacionalidad == "chileno" and edad >= 18 and sueldo > 500000:
    print("Si puede optar al BONO IFE")
else:
    print("NO puedes optar al BONO IFE")

direccion = "romeral"
#Asignar BONO movilizacion a todos aquellos que no viven en curico
if not(nacionalidad == "chileno"):
    print("Puede optar")
else:
    print("NO Puede optar")

if not(direccion == "curico"):
    print("Asignar Movilizacion")


if not(direccion == "curico"): print("Asignar Movilizacion")
else: print("NO asignar movilizacion")

