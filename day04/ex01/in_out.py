# in_out.py

from typing import Any

def square(x: int | float) -> int | float:
    """Retourne le carré de x"""
    return x ** 2

def pow(x: int | float) -> float:
    """Retourne x élevé à la puissance x"""
    return x ** x

def outer(x: int | float, function) -> object:
    """
    Prend un nombre et une fonction, et retourne un objet (fonction)
    qui, lorsqu'il est appelé, applique la fonction sur la valeur précédente
    et met à jour cette valeur.
    """
    count = x  # stockage de la valeur interne

    def inner() -> float:
        nonlocal count  # permet de modifier la variable externe
        count = function(count)
        return count

    return inner
