grafos = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'A': [],
} 

def dfs (grafo, nodo,visitados=None):
    if visitados is None:
        visitados = set ()
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs (grafos,vecino,visitados)
    return

resultado = dfs (grafos, 'A')
print(f"Nodos visitados por DFS: {resultado}")