from load_csv import load
import matplotlib.pyplot as plt


def aff_life(path: str) :
    df = load(path)
    morocco_data = df[df["country"] == "Morocco"]
     # Extraire les années et les valeurs
    years = [int(col) for col in df.columns[1:]]        # toutes les colonnes sauf "country"
    life_expectancy = morocco_data.iloc[0, 1:]  # la première ligne, toutes les colonnes sauf "country"

    plt.figure(figsize=(10, 5))  # taille plus grande pour éviter les artefacts

    plt.plot(years, life_expectancy.values.flatten(), label="Espérance de vie", marker='o')
    plt.title("Morocco life expectancy projection")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()  # affiche la légende
    plt.xticks(rotation=60)  # pivote les années pour mieux voir
    plt.tight_layout()       # ajuste la mise en page
    plt.show()