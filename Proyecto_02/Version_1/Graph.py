from Node import Nodo
from Segment import Segmento
from math import sqrt
import matplotlib.pyplot as plt

class Gráfico:

    Lista_de_nodos = []
    Lista_de_segmentos = []
    Lista_de_nombre_de_nodos = []
    Lista_de_nombre_de_segmentos = []


    def Añadir_nodo(self, n: Nodo):
        Añadido, Encontrado = True, False

        if len(Gráfico.Lista_de_nodos) == 0:
            Gráfico.Lista_de_nodos.append(n)
            Gráfico.Lista_de_nombre_de_nodos.append(n.Nombre_nodo)
            Añadido = True
            Encontrado = True

        if len(Gráfico.Lista_de_nodos) != 0:
            for i in Gráfico.Lista_de_nodos:
                if i.Nombre_nodo == n.Nombre_nodo:
                    Encontrado = True
                    Añadido = False
            
            if Encontrado == False:
                Gráfico.Lista_de_nodos.append(n)
                Gráfico.Lista_de_nombre_de_nodos.append(n.Nombre_nodo)


        return Añadido
                        
    def Añadir_segmento(self,Nombre, Nombre_nodo_origen, Nombre_nodo_destino):

        Nodo_origen = Gráfico.Nodo_por_nombre(Nombre_nodo_origen)
        Nodo_destino = Gráfico.Nodo_por_nombre(Nombre_nodo_destino)

        s1 = Segmento(Nombre_nodo_origen+Nombre_nodo_destino, Nodo_origen, Nodo_destino)

        Nodo.Añadir_vecino(Nodo_origen, Nodo_destino)

        Gráfico.Lista_de_segmentos.append(s1)
        Gráfico.Lista_de_nombre_de_segmentos.append(s1.Nombre_segmento)

        return True
    
    def Obtener_más_cercano(self, Punto_x, Punto_y):
        Distancias = []
        for i in Gráfico.Lista_de_nodos:
            Distancias.append(Gráfico.Distancia_punto_a_punto(i.Coordenada_x, i.Coordenada_y, Punto_x, Punto_y))

        Distancia_más_corta = sorted(Distancias)[0]

        Índice_nodo_distancia_más_corta = Distancias.index(Distancia_más_corta)

        return Gráfico.Lista_de_nodos[Índice_nodo_distancia_más_corta]

    def Gráficar(self):

        for i in Gráfico.Lista_de_nodos:
            plt.scatter(i.Coordenada_x, i.Coordenada_y, color="Gray")

        for i in Gráfico.Lista_de_segmentos:
            Nodo_origen = Gráfico.Nodo_por_nombre(i.Origen)
            Nodo_destino = Gráfico.Nodo_por_nombre(i.Destino)

            Coordenadas_x = [Nodo_origen.Coordenada_x, Nodo_destino.Coordenada_x]
            Coordenadas_y = [Nodo_origen.Coordenada_y, Nodo_destino.Coordenada_y]

            plt.plot(Coordenadas_x,Coordenadas_y)

        plt.xlim(-5, 25)
        plt.ylim(-5, 25)
        plt.grid(True, color="Red")
        plt.show()

    def Gráficar_nodo(self, Nombre_nodo_origen):

        Nodo_origen = Gráfico.Nodo_por_nombre(Nombre_nodo_origen)

        for i in Gráfico.Lista_de_nodos:
            plt.scatter(i.Coordenada_x, i.Coordenada_y, color="Gray")

        for i in Nodo_origen.Vecinos:

            Coordenadas_x = [Nodo_origen.Coordenada_x, i.Coordenada_x]
            Coordenadas_y = [Nodo_origen.Coordenada_y, i.Coordenada_y]

            plt.plot(Coordenadas_x, Coordenadas_y, color="Red", label=Nodo.Distancia_entre_nodos(Nodo_origen,i))

            Mid_x = (Nodo_origen.Coordenada_x + i.Coordenada_x) / 2
            Mid_y = (Nodo_origen.Coordenada_y + i.Coordenada_y) / 2

            Longitud = Gráfico.Distancia_punto_a_punto(Nodo_origen.Coordenada_x, Nodo_origen.Coordenada_y, i.Coordenada_x, i.Coordenada_y)

            plt.text(Mid_x, Mid_y, f"{Longitud:.2f}", ha='center', va='center', backgroundcolor="white")

        for i in Nodo_origen.Vecinos:
            plt.scatter(i.Coordenada_x, i.Coordenada_y, color="Green")

        plt.scatter(Nodo_origen.Coordenada_x, Nodo_origen.Coordenada_y, color="Blue")

        plt.xlim(-5, 25)
        plt.ylim(-5, 25)
        plt.legend()
        plt.grid(True, color="Red")
        plt.show()

    def Nodo_por_nombre(Nombre_nodo):
        for i in Gráfico.Lista_de_nodos:
            if Nombre_nodo == i.Nombre_nodo:
                Nodo_buscado = i

        return Nodo_buscado
    
    def Distancia_punto_a_punto(Punto1_x, Punto1_y, Punto2_x, Punto2_y):
        Distancia = sqrt((Punto1_x-Punto2_x)**2 + (Punto1_y-Punto2_y)**2)

        return Distancia
        
    

