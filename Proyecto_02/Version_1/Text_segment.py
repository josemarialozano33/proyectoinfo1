from Node import Nodo
from Segment import Segmento

A = Nodo("A", 1, 8)
B = Nodo("B", 9, 5)
C = Nodo("C", 4, 2)

AB = Segmento("AB", A, B)
BC = Segmento("BC", B, C)

print(AB.__dict__, BC.__dict__)