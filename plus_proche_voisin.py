import numpy as np

def plus_proche_voisin(d: np.ndarray) -> list:
    """
    Applique l'algorithme du plus proche voisin pour trouver un chemin d'exploration.
    
    Paramètres:
    d (np.ndarray): Matrice des distances entre les points d'intérêt.
    
    Retourne:
    list: Chemin d'exploration en appliquant l'algorithme du plus proche voisin.
    """
    n = len(d) - 1  # Nombre de points d'intérêt
    chemin = []
    visited = [False] * n
    
    # Commencer à la position courante du robot (indice n)
    current = n
    
    for _ in range(n):
        # Trouver le point non visité le plus proche
        nearest = -1
        nearest_distance = float('inf')
        for i in range(n):
            if not visited[i] and d[current, i] < nearest_distance:
                nearest = i
                nearest_distance = d[current, i]
        
        # Marquer le point comme visité et l'ajouter au chemin
        visited[nearest] = True
        chemin.append(nearest)
        current = nearest
    
    return chemin

# Exemple d'utilisation
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 30, 20, 10, 0]
])
print(plus_proche_voisin(distances))  # Exemple de chemin trouvé par l'algorithme du plus proche voisin