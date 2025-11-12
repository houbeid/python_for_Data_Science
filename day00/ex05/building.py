import sys


def building(str):
    punctuations = '.,;:!?\'"()-[]{}<>@$#%^&*_+=\\|~`'
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0
    ch = 0
    for c in str:
        ch += 1
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        elif c in punctuations:
            punc += 1
        else:
            continue
    print("the text contains", ch,  "characters:")
    print(upper, " upper letters")
    print(lower, " lower letters")
    print(punc, " punctuations marks")
    print(space, " spaces")
    print(digit, " digits")


def main():
    # lecture des arguments
    # vérification du nombre d'arguments
    # si aucun argument -> demander à l'utilisateur
    # traitement de la chaîne
    # affichage des résultats
    if len(sys.argv) > 2:
        print("AssertionError: more than one atgument is provided")
        exit()
    if len(sys.argv) < 2:
        str = input("what is the text to count")
    else:
        str = sys.argv[1]
    building(str)


if __name__ == "__main__":
    main()
