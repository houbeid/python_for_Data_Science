import sys

def list_of_words(s: str, N: int) -> list:
    words = [word for word in s.split()]
    long_words = list(filter(lambda w: len(w) > N, words))
    return long_words

def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    # Appel de la fonction avec affichage du résultat
    print(list_of_words(sys.argv[1], N))

if __name__ == "__main__":
    main()
