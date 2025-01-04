def F1(photo:np.ndarray) -> np.ndarray:
    n = photo.min()                   # Ligne 2
    b = photo.max()                   # Ligne 3
    h = np.zeros(b - n + 1, np.int64) # Ligne 4
    for p in photo.flat:              # Ligne 5
        h[p - n] += 1                 # Ligne 6
    return h                          # Ligne 7