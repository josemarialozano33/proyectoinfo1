
Lista_de_nodos = []

class Nodo:

    def __init__(self, Nombre: str, Coordenada_x: float, Coordenada_y: float):
        self.Nombre_nodo = Nombre
        self.Coordenada_x = Coordenada_x
        self.Coordenada_y = Coordenada_y
        self.Vecinos = []

        Lista_de_nodos.append(Nombre)

    def Añadir_vecino(n1, n2:__init__):
        Añadido, Encontrado = True, False
        n = 0
        if len(n1.Vecinos) == 0:
            n1.Vecinos.append(n2)
            Añadido = True
            Encontrado = True

        for n in n1.Vecinos:
            if n == n2.Nombre_nodo:
                Añadido = False
                Encontrado = True

        if not Encontrado:
            n1.Vecinos.append(n2)

        return Añadido
    
    def Distancia_entre_nodos(n1, n2:__init__):
        from math import sqrt

        Distancia = sqrt((n1.Coordenada_x-n2.Coordenada_x)**2 + (n1.Coordenada_y-n2.Coordenada_y)**2)
        
        return Distancia