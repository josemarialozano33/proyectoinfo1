from random import randint

class Crear_datos_aleatorios:
    def Crear_puntos_aleatorios(Número_de_datos : int, Rango : int):
        
        with open("C:\Uni\Informàtica\Proyecto_02\Data\Puntos_aleatorios.txt", "w") as datos: pass

        for n in range(Número_de_datos - 1):
            punto = f"{randint(0, Rango)}-{randint(0, Rango)}/"

            if n == Número_de_datos-2:
                punto += f"{randint(0, Rango)}-{randint(0, Rango)}"

            with open("C:\Uni\Informàtica\Proyecto_02\Data\Puntos_aleatorios.txt", "a") as datos:
                datos.write(punto)

            print(n, punto)

Crear_datos_aleatorios.Crear_puntos_aleatorios(10, 10)
            