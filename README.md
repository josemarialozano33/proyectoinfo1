# Proyecto 02 – Explorador de Rutas en el Espacio Aéreo  
**Versión 1** – Documentación detallada

> **Asignatura:** Informática 1 (Q2 2024‑25)  
> **Autores:** _[Adria Bagüest, Arnau Pons y José María Lozano]_    

---

## Índice
1. [Introducción](#introducción)  
2. [Estructura del proyecto](#estructura-del-proyecto)  
3. [Módulo `Node.py`](#módulo-nodepy)  
   1. [Clase `Nodo`](#clase-nodo)  
   2. [Funciones auxiliares](#funciones-auxiliares)  
4. [Módulo `Segment.py`](#módulo-segmentpy)  
   1. [Clase `Segmento`](#clase-segmento)  
5. [Módulo `Graph.py`](#módulo-graphpy)  
   1. [Almacenamiento de datos](#almacenamiento-de-datos)  
   2. [Añadir nodos y segmentos](#añadir-nodos-y-segmentos)  
   3. [Búsquedas y utilidades](#búsquedas-y-utilidades)  
   4. [Visualización gráfica](#visualización-gráfica)  
6. [Scripts de prueba](#scripts-de-prueba)  
7. [Utilidades adicionales](#utilidades-adicionales)  
8. [Requisitos e instalación](#requisitos-e-instalación)  
9. [Uso y ejemplos](#uso-y-ejemplos)  
10. [Próximos pasos](#próximos-pasos)  

---

## Introducción
Este repositorio contiene la **Versión 1** del proyecto.
Se ha implementado:

* Un **grafo dirigido** donde cada nodo representa un _waypoint_ con coordenadas (x, y).  
* Segmentos ponderados por coste (distancia).  
* Funcionalidades de **creación**, **búsqueda**, **visualización** y **pruebas** unitarias.

---

## Estructura del proyecto
    Proyecto_02/
        Version_1/
            Node.py            # Definición de la clase Nodo
            Segment.py         # Definición de la clase Segmento
            Graph.py           # Clase Gráfico y operaciones sobre el grafo
            Text_segment.py    # Prueba de Segmento
            test_graph.py      # Prueba completa del grafo
        Utilities/
            Datos_aleatorios.py  # Genera puntos aleatorios para grafos
            importar_datos.py    # (vacío por implementar)
        Data/                   # Carpeta para ficheros de grafo externos

---

## Módulo `Node.py`

### Clase `Nodo`
Define un nodo con:

* `self.Nombre_nodo: str`  
* `self.Coordenada_x: float`  
* `self.Coordenada_y: float`  
* `self.Vecinos: list[Nodo]`  

Al instanciarse:

    n = Nodo("A", 1.0, 2.0)  # Añade "A" a la lista global Lista_de_nodos

Internamente el módulo mantiene la lista global:

    Lista_de_nodos = [] 
    
### Funciones auxiliares
1. **`Añadir_vecino(n1, n2)`**  
   * Comprueba si `n2.Nombre_nodo` ya existe en `n1.Vecinos`.  
   * Si no existe, lo añade y devuelve `True`; si ya estaba, devuelve `False`.

2. **`Distancia_entre_nodos(n1, n2)`**  
   * Retorna √((x₂−x₁)² + (y₂−y₁)²).

_Ejemplo_:

    from Node import Nodo, Añadir_vecino, Distancia_entre_nodos
    a = Nodo("A", 0, 0)
    b = Nodo("B", 3, 4)
    print(Distancia_entre_nodos(a, b))  # 5.0
    print(Añadir_vecino(a, b))          # True
    print(Añadir_vecino(a, b))          # False

---

## Módulo `Segment.py`

### Clase `Segmento`
Un segmento une dos nodos de forma **dirigida**:

* `self.Nombre_segmento: str` – etiqueta (ej. “AB”).  
* `self.Origen: str` – nombre del nodo origen.  
* `self.Destino: str` – nombre del nodo destino.  
* `self.Costo: float` – distancia calculada en el constructor.

Uso típico:

    s = Segmento("AB", nodoA, nodoB)  # Calcula Costo internamente

El segmento es **inmutable**: no se prevé modificar su coste ni sus extremos.

---

## Módulo `Graph.py`

### Almacenamiento de datos
`Gráfico` centraliza toda la información mediante **listas de clase**:

    class Gráfico:
        Lista_de_nodos = []               # objetos Nodo
        Lista_de_segmentos = []           # objetos Segmento
        Lista_de_nombre_de_nodos = []     # nombres 
        Lista_de_nombre_de_segmentos = [] # nombres 


### Añadir nodos y segmentos
* **`Añadir_nodo(self, n)`**  
  Añade `n` si su nombre no existe y devuelve `True`; si existe, `False`.

* **`Añadir_segmento(self, nombre, origen, destino)`**  
  1. Busca los nodos por nombre (`Nodo_por_nombre`).  
  2. Crea el `Segmento`.  
  3. Llama a `Añadir_vecino` para enlazar los nodos.  
  4. Registra el segmento y su nombre.

### Búsquedas y utilidades
* **`Nodo_por_nombre(nombre)`** – búsqueda lineal en `Lista_de_nodos`.  
* **`Obtener_más_cercano(self, x, y)`** – devuelve el nodo más próximo al punto (x,y).  
* **`Distancia_punto_a_punto`** – utilidad matemática (sqrt).

### Visualización gráfica
Requiere **matplotlib**.

* **`Gráficar(self)`**  
  Dibuja todo el grafo:  
  * Nodos en gris.  
  * Segmentos en negro con el coste impreso en el centro.

* **`Gráficar_nodo(self, origen)`**  
  * Origen en azul.  
  * Vecinos en verde.  
  * Aristas origen→vecino en rojo con los costes señalados.

---

## Scripts de prueba

1. **`Text_segment.py`**  
   * Crea nodos A‑B‑C y segmentos AB, BC.  
   * Imprime los atributos para inspección rápida.

2. **`test_graph.py`**  
   * Construye el grafo de ejemplo A–L descrito en la guía.  
   * Llama a `Gráficar()` y a `Gráficar_nodo("C")`.  
   * Verifica que `Obtener_más_cercano(15,5)` es “J” y `(8,19)` es “B”.

Ejecución:

    python Text_segment.py
    python test_graph.py

---

## Utilidades adicionales

* **`Utilities/Datos_aleatorios.py`**  
  Genera un fichero con coordenadas aleatorias (`x-y/…`) para completar grafos grandes.

* **`Utilities/importar_datos.py`**  
  Base para la Versión 2 (lectura/escritura de grafos).

---

## Requisitos e instalación
* **Python ≥ 3.10** (probado en 3.12)  
* **matplotlib ≥ 3.8**

Pasos rápidos:

    git clone https://github.com/<usuario>/Proyecto_02.git
    cd Proyecto_02/Version_1
    python -m venv venv      # opcional
    source venv/bin/activate # Linux/macOS
    venv\Scripts\activate    # Windows
    pip install matplotlib

---

## Uso y ejemplos

Ejecuta en la carpeta `Version_1`:

    # Prueba de segmento
    python Text_segment.py

    # Prueba completa + gráficos
    python test_graph.py

Aparecerán dos ventanas gráficas: una con el grafo completo y otra con el vecindario del nodo “C”.

---

## Próximos pasos
| Versión | Objetivo principal |
|---------|--------------------|
| v2 | Lectura y guardado de grafos desde/ a fichero |
| v3 | GUI completa en Tkinter (alta/baja visual de nodos y segmentos) |
| v4 | Algoritmos de ruta óptima (Dijkstra, A\*) |
| vFinal | Refactor, documentación Sphinx, CI en GitHub Actions |
