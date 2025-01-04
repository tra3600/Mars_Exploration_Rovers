import numpy as np

def longueur_chemin(chemin: list, d: np.ndarray) -> float:
    """
    Calcule la longueur totale d'un chemin en utilisant la matrice des distances.
    
    Paramètres:
    chemin (list): Liste des indices des points d'intérêt dans l'ordre de leur parcours.
    d (np.ndarray): Matrice des distances entre les points d'intérêt.
    
    Retourne:
    float: Distance totale du chemin.
    """
    distance_totale = 0.0
    # Point de départ (position courante du robot)
    position_actuelle = len(d) - 1
    
    for point in chemin:
        distance_totale += d[position_actuelle, point]
        position_actuelle = point
    
    # Retour au point de départ
    distance_totale += d[position_actuelle, len(d) - 1]
    
    return distance_totale

# Exemple d'utilisation
chemin = [0, 1, 2, 3]
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 30, 20, 10, 0]
])
print(longueur_chemin(chemin, distances))  # Devrait afficher la distance totale du chemin