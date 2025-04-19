from Node import Nodo

class Segmento:

    def __init__(self, Nombre: str, Nodo_origen: Nodo, Nodo_destino: Nodo):
        self.Nombre_segmento = Nombre
        self.Origen = Nodo_origen.Nombre_nodo
        self.Destino = Nodo_destino.Nombre_nodo

        Distancia = Nodo.Distancia_entre_nodos(Nodo_origen, Nodo_destino)

        self.Costo = Distancia






        


        


    

    

