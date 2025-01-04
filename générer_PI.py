import numpy as np
import random

def générer_PI(n:int, cmax:int) -> np.ndarray:
    """
    Génère une exploration aléatoire avec n points d'intérêts dans une zone carrée de largeur cmax.
    
    Paramètres:
    n (int): Nombre de points d'intérêts à générer.
    cmax (int): Largeur de la zone d'exploration (en millimètres).
    
    Retourne:
    np.ndarray: Tableau numpy contenant les coordonnées des points d'intérêts.
    """
    points = set()
    while len(points) < n:
        x = random.randrange(0, cmax)
        y = random.randrange(0, cmax)
        points.add((x, y))
    
    return np.array(list(points))

# Exemple d'utilisation
n = 4
cmax = 1000
exploration = générer_PI(n, cmax)
print(exploration)