from Graph import *

def Crear_Gráfico_1():
    G = Gráfico()

    Gráfico.Añadir_nodo(G, Nodo("A",1,20))  
    Gráfico.Añadir_nodo(G, Nodo("B",8,17))  
    Gráfico.Añadir_nodo(G, Nodo("C",15,20))  
    Gráfico.Añadir_nodo(G, Nodo("D",18,15))  
    Gráfico.Añadir_nodo(G, Nodo("E",2,4))  
    Gráfico.Añadir_nodo(G, Nodo("F",6,5))  
    Gráfico.Añadir_nodo(G, Nodo("G",12,12))  
    Gráfico.Añadir_nodo(G, Nodo("H",10,3))  
    Gráfico.Añadir_nodo(G, Nodo("I",19,1))  
    Gráfico.Añadir_nodo(G, Nodo("J",13,5))  
    Gráfico.Añadir_nodo(G, Nodo("K",3,15))  
    Gráfico.Añadir_nodo(G, Nodo("L",4,10))  

    Gráfico.Añadir_segmento(G, "AB", "A", "B")  
    Gráfico.Añadir_segmento(G, "AE", "A", "E")  
    Gráfico.Añadir_segmento(G, "AK", "A", "K")  
    Gráfico.Añadir_segmento(G, "BA", "B", "A")  
    Gráfico.Añadir_segmento(G, "BC", "B", "C")  
    Gráfico.Añadir_segmento(G, "BF", "B", "F")  
    Gráfico.Añadir_segmento(G, "BK", "B", "K")  
    Gráfico.Añadir_segmento(G, "BG", "B", "G")  
    Gráfico.Añadir_segmento(G, "CD", "C", "D")  
    Gráfico.Añadir_segmento(G, "CG", "C", "G")  
    Gráfico.Añadir_segmento(G, "DG", "D", "G")  
    Gráfico.Añadir_segmento(G, "DH", "D", "H")  
    Gráfico.Añadir_segmento(G, "DI", "D", "I")  
    Gráfico.Añadir_segmento(G, "EF", "E", "F")  
    Gráfico.Añadir_segmento(G, "FL", "F", "L")  
    Gráfico.Añadir_segmento(G, "GB", "G", "B")  
    Gráfico.Añadir_segmento(G, "GF", "G", "F")  
    Gráfico.Añadir_segmento(G, "GH", "G", "H")  
    Gráfico.Añadir_segmento(G, "ID", "I", "D")  
    Gráfico.Añadir_segmento(G, "IJ", "I", "J")  
    Gráfico.Añadir_segmento(G, "JI", "J", "I")  
    Gráfico.Añadir_segmento(G, "KA", "K", "A")  
    Gráfico.Añadir_segmento(G, "KL", "K", "L")  
    Gráfico.Añadir_segmento(G, "LK", "L", "K")  
    Gráfico.Añadir_segmento(G, "LF", "L", "F") 

    return G 

print("Probando el grafo...")  

G = Crear_Gráfico_1()  

Gráfico.Gráficar(G)  

Gráfico.Gráficar_nodo(G, "C")  

n = Gráfico.Obtener_más_cercano(G, 15, 5)  
print(n.Nombre_nodo)  # La respuesta debe ser J  

n = Gráfico.Obtener_más_cercano(G, 8, 19)  
print(n.Nombre_nodo)  # La respuesta debe ser B  




