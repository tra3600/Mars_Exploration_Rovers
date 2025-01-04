import random
import numpy as np

def créer_population(m: int, d: np.ndarray) -> list:
    """
    Crée une population de m individus aléatoires.
    
    Paramètres:
    m (int): Nombre d'individus à engendrer.
    d (np.ndarray): Matrice des distances entre points d'intérêt.
    
    Retourne:
    list: Liste d'individus (longueur, chemin).
    """
    n = len(d) - 1  # Nombre de points d'intérêt
    population = []

    for _ in range(m):
        chemin = list(range(n))
        random.shuffle(chemin)
        longueur = longueur_chemin(chemin, d)
        population.append((longueur, chemin))
    
    return population

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
    current = len(d) - 1
    
    for point in chemin:
        distance_totale += d[current, point]
        current = point
    
    # Retour au point de départ
    distance_totale += d[current, len(d) - 1]
    
    return distance_totale

# Exemple d'utilisation
distances = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 30, 20, 10, 0]
])
population = créer_population(5, distances)
print(population)

def réduire(p: list) -> None:
    """
    Réduit une population de moitié en ne conservant que les individus avec les chemins les plus courts.
    
    Paramètres:
    p (list): Liste d'individus (longueur, chemin).
    
    Retourne:
    None: Modifie la liste passée en paramètre.
    """
    p.sort(key=lambda x: x[0])  # Trier les individus par longueur de chemin (ascendant)
    del p[len(p)//2:]  # Supprimer la moitié inférieure des individus

# Exemple d'utilisation
population = créer_population(10, distances)
print("Population avant réduction:", population)
réduire(population)
print("Population après réduction:", population)


def muter_chemin(c: list) -> None:
    """
    Transforme un chemin en inversant aléatoirement deux de ses éléments.
    
    Paramètres:
    c (list): Chemin à muter.
    
    Retourne:
    None: Modifie la liste passée en paramètre.
    """
    i, j = random.sample(range(len(c)), 2)
    c[i], c[j] = c[j], c[i]

# Exemple d'utilisation
chemin = [0, 1, 2, 3, 4]
print("Chemin avant mutation:", chemin)
muter_chemin(chemin)
print("Chemin après mutation:", chemin)

def muter_population(p: list, proba: float, d: np.ndarray) -> None:
    """
    Fait muter un certain nombre d'individus dans la population en fonction de la probabilité de mutation.
    
    Paramètres:
    p (list): Population d'individus (longueur, chemin).
    proba (float): Probabilité de mutation d'un individu.
    d (np.ndarray): Matrice des distances entre points d'intérêt.
    
    Retourne:
    None: Modifie la liste passée en paramètre.
    """
    for i in range(len(p)):
        if random.random() < proba:
            muter_chemin(p[i][1])
            p[i] = (longueur_chemin(p[i][1], d), p[i][1])

# Exemple d'utilisation
population = créer_population(10, distances)
print("Population avant mutation:", population)
muter_population(population, 0.3, distances)
print("Population après mutation:", population)

def croiser(c1: list, c2: list) -> list:
    """
    Crée un nouveau chemin à partir de deux chemins passés en paramètre.
    
    Paramètres:
    c1 (list): Premier chemin.
    c2 (list): Deuxième chemin.
    
    Retourne:
    list: Nouveau chemin normalisé.
    """
    n = len(c1)
    half = n // 2
    new_chemin = c1[:half] + c2[half:]
    return normaliser_chemin(new_chemin, n)

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
c1 = [0, 1, 2, 3, 4]
c2 = [4, 3, 2, 1, 0]
new_chemin = croiser(c1, c2)
print("Nouveau chemin après croisement:", new_chemin)

def nouvelle_génération(p: list, d: np.ndarray) -> None:
    """
    Fait croiser les membres de la population pour en doubler l'effectif.
    
    Paramètres:
    p (list): Population d'individus (longueur, chemin).
    d (np.ndarray): Matrice des distances entre points d'intérêt.
    
    Retourne:
    None: Modifie la liste passée en paramètre.
    """
    n = len(p)
    new_population = []
    for i in range(n):
        c1, c2 = p[i][1], p[(i+1)%n][1]
        new_chemin = croiser(c1, c2)
        longueur = longueur_chemin(new_chemin, d)
        new_population.append((longueur, new_chemin))
    
    p.extend(new_population)

# Exemple d'utilisation
population = créer_population(5, distances)
print("Population avant nouvelle génération:", population)
nouvelle_génération(population, distances)
print("Population après nouvelle génération:", population)


def algo_génétique(PI: np.ndarray, m: int, proba: float, g: int) -> (float, list):
    """
    Implante un algorithme génétique pour trouver un chemin d'exploration optimal.
    
    Paramètres:
    PI (np.ndarray): Tableau de points d'intérêts.
    m (int): Taille de la population.
    proba (float): Probabilité de mutation.
    g (int): Nombre de générations.
    
    Retourne:
    float: Longueur du plus court chemin trouvé.
    list: Chemin correspondant.
    """
    # Calculer la matrice des distances
    d = calculer_distances(PI)
    
    # Créer la population initiale
    population = créer_population(m, d)
    
    for _ in range(g):
        # Réduire la population
        réduire(population)
        # Faire croiser la population pour en doubler l'effectif
        nouvelle_génération(population, d)
        # Appliquer les mutations
        muter_population(population, proba, d)
    
    # Trouver le meilleur chemin
    meilleur_individu = min(population, key=lambda x: x[0])
    return meilleur_individu

# Exemple d'utilisation
PI = np.array([[345, 635], [1076, 415], [38, 859], [121, 582]])
resultat = algo_génétique(PI, 10, 0.1, 50)
print("Meilleur chemin trouvé:", resultat)


def algo_génétique(PI: np.ndarray, m: int, proba: float, g: int) -> (float, list):
    """
    Implante un algorithme génétique pour trouver un chemin d'exploration optimal.
    
    Paramètres:
    PI (np.ndarray): Tableau de points d'intérêts.
    m (int): Taille de la population.
    proba (float): Probabilité de mutation.
    g (int): Nombre de générations.
    
    Retourne:
    float: Longueur du plus court chemin trouvé.
    list: Chemin correspondant.
    """
    # Calculer la matrice des distances
    d = calculer_distances(PI)
    
    # Créer la population initiale
    population = créer_population(m, d)
    
    meilleur_individu = min(population, key=lambda x: x[0])
    
    for _ in range(g):
        # Réduire la population
        réduire(population)
        # Ajouter le meilleur individu trouvé jusqu'à présent
        population.append(meilleur_individu)
        # Faire croiser la population pour en doubler l'effectif
        nouvelle_génération(population, d)
        # Appliquer les mutations
        muter_population(population, proba, d)
        # Mettre à jour le meilleur individu
        meilleur_individu = min(population, key=lambda x: x[0])
    
    return meilleur_individu

# Exemple d'utilisation
PI = np.array([[345, 635], [1076, 415], [38, 859], [121, 582]])
resultat = algo_génétique(PI, 10, 0.1, 50)
print("Meilleur chemin trouvé:", resultat)


