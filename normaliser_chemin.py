def normaliser_chemin(chemin: list, n: int) -> list:
    """
    Normalise un chemin pour qu'il contienne une seule fois tous les entiers entre 0 et n (exclu).
    
    Paramètres:
    chemin (list): Liste des indices des points d'intérêt.
    n (int): Nombre total de points d'intérêt.
    
    Retourne:
    list: Chemin normalisé.
    """
    chemin_normalise = []
    vus = set()
    
    # Supprimer les doublons et les valeurs >= n
    for point in chemin:
        if point not in vus and point < n:
            chemin_normalise.append(point)
            vus.add(point)
    
    # Ajouter les éléments manquants
    for point in range(n):
        if point not in vus:
            chemin_normalise.append(point)
    
    return chemin_normalise

# Exemple d'utilisation
chemin = [0, 2, 2, 3, 4, 1, 5, 1]
n = 5
print(normaliser_chemin(chemin, n))  # Devrait afficher un chemin normalisé