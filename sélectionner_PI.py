import numpy as np

def sélectionner_PI(photo: np.ndarray, imin: int, imax: int) -> np.ndarray:
    """
    Sélectionne les points d'intérêt dans la photographie dont l'intensité est comprise entre imin et imax.
    
    Paramètres:
    photo (np.ndarray): Tableau représentant une photographie.
    imin (int): Intensité minimale.
    imax (int): Intensité maximale.
    
    Retourne:
    np.ndarray: Tableau à deux dimensions contenant les coordonnées des points d'intérêt.
    """
    # Liste pour stocker les coordonnées des points d'intérêt
    points_interet = []

    # Parcourir l'image pour trouver les points d'intérêt
    for x in range(photo.shape[0]):
        for y in range(photo.shape[1]):
            if imin <= photo[x, y] <= imax:
                points_interet.append([x, y])

    # Convertir la liste en tableau numpy
    return np.array(points_interet)

# Exemple d'utilisation
photo = np.array([
    [100, 150, 200],
    [50, 255, 80],
    [130, 170, 90]
])
imin = 100
imax = 200
points_interet = sélectionner_PI(photo, imin, imax)
print(points_interet)