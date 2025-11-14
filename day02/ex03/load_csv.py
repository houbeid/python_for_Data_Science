import pandas as pd


def load(path: str) -> pd.array:
    """
    Charge un fichier CSV en DataFrame, affiche ses dimensions
    et le retourne. Retourne None si le chemin ou le format est invalide.
    """
    try:
        df = pd.read_csv(path)
        print ("Loading dataset of dimensions ", df.shape)
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        print("Erreur : chemin ou format du fichier invalide.")
        return 