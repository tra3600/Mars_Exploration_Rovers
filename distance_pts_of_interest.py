import numpy as np
import math

def position_robot() -> tuple:
    # Exemple de position du robot, à remplacer par l'implémentation réelle
    return (500, 500)

def calculer_distances(PI: np.ndarray) -> np.ndarray:
    """
    Calcule le tableau des distances entre les points d'intérêt et la position du robot.
    
    Paramètres:
    PI (np.ndarray): Tableau de n points d'intérêt avec leurs coordonnées.
    
    Retourne:
    np.ndarray: Tableau des distances de dimension (n + 1) x (n + 1).
    """
    n = len(PI)
    distances = np.zeros((n + 1, n + 1))
    robot_x, robot_y = position_robot()

    # Calcul des distances entre les points d'intérêt
    for i in range(n):
        for j in range(i, n):
            dist = math.sqrt((PI[j, 0] - PI[i, 0])**2 + (PI[j, 1] - PI[i, 1])**2)
            distances[i, j] = dist
            distances[j, i] = dist  # Symétrie

    # Calcul des distances entre les points d'intérêt et la position du robot
    for i in range(n):
        dist_to_robot = math.sqrt((PI[i, 0] - robot_x)**2 + (PI[i, 1] - robot_y)**2)
        distances[i, n] = dist_to_robot
        distances[n, i] = dist_to_robot  # Symétrie

    return distances

# Exemple d'utilisation
PI = np.array([[345, 635], [1076, 415], [38, 859], [121, 582]])
distances = calculer_distances(PI)
print(distances)