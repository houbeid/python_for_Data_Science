import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    Tronque un tableau 2D (liste de listes) selon les indices start et end,
    affiche les dimensions avant et après le découpage, et retourne la nouvelle liste.

    Args:
        family (list): Tableau 2D à découper (liste de listes de même taille).
        start (int): Indice de début du découpage.
        end (int): Indice de fin du découpage.

    Returns:
        list: Le tableau tronqué entre start et end.

    Raises:
        AssertionError: Si l’entrée n’est pas une liste de listes valides ou si les sous-listes
                        n’ont pas toutes la même taille.
    """
    # Vérification du type
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise AssertionError("family doit être une liste de listes.")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(family[0])
    if any(len(row) != row_length for row in family):
        raise AssertionError("Toutes les sous-listes doivent avoir la même taille.")

    # Conversion en tableau numpy
    arr = np.array(family)

    # Affichage des dimensions
    print(f"My shape is : {arr.shape}")

    # Application du slicing
    new_arr = arr[start:end]

    # Affichage des nouvelles dimensions
    print(f"My new shape is : {new_arr.shape}")

    # Retour sous forme de liste Python
    return new_arr.tolist()
