# === Définition de ft_filter ===
def ft_filter(function, iterable):
    """Recode de la fonction filter()"""
    if function is None:
        # Si aucune fonction, on garde seulement les éléments "vrais"
        return (item for item in iterable if item)
    else:
        # Sinon, on garde les éléments pour lesquels function(item) == True
        return (item for item in iterable if function(item))


# === Fonctions de test ===
def is_even(n):
    """Retourne True si le nombre est pair"""
    return n % 2 == 0


def is_positive(n):
    """Retourne True si le nombre est positif"""
    return n > 0


# === Tests ===

def main():
    # Liste d'exemple
    numbers = [-3, -2, -1, 0, 1, 2, 3, 4]

    # --- Test 1 : avec une fonction (nombres pairs)
    print("Test 1 : nombres pairs")
    print("filter :", list(filter(is_even, numbers)))
    print("ft_filter :", list(ft_filter(is_even, numbers)))
    print()

    # --- Test 2 : avec une autre fonction (nombres positifs)
    print("Test 2 : nombres positifs")
    print("filter :", list(filter(is_positive, numbers)))
    print("ft_filter :", list(ft_filter(is_positive, numbers)))
    print()

    # --- Test 3 : avec None (suppression des valeurs 'fausses')
    print("Test 3 : filter(None, iterable)")
    data = [0, 1, "", "hello", [], [1, 2], False, True, None]
    print("filter :", list(filter(None, data)))
    print("ft_filter :", list(ft_filter(None, data)))
    print()

    # --- Test 4 : vérification que les deux se comportent pareil
    print("Test 4 : comparaison automatique")
    print(list(filter(is_even, numbers)) == list(ft_filter(is_even, numbers)))
    print(list(filter(None, data)) == list(ft_filter(None, data)))


if __name__ == "__main__":
    main()
