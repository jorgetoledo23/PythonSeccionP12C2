semaforo = True
while semaforo:
    #Se repetira mientras la condicion sea evaluada como Verdadera
    print("Estamos en un ciclo While")
    semaforo = False
    if 5 < 10:
        break
    #break
#Continuara su camino Normal
print("Aca estamos fuera del While")


edad = True #bool
while edad:
    try:
        edad = int(input("Ingrese su Edad: "))
        break
    except ValueError:
        print("El Dato ingresado NO corresponde a una Edad VALIDA!")
    except NameError:
        print("Error de variable no definida!")
    except:
        pass
print("Dato ingresado con Exito!")