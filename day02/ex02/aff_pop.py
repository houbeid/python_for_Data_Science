from load_csv import load
import matplotlib.pyplot as plt


def aff_pop(path: str) :
    df = load(path)
    # convertir les colonnes "années" en int
    years = [int(col) for col in df.columns[1:]]

    # extraire les données
    country_campus = df[df["country"] == "Morocco"].iloc[:, 1:]
    country_other = df[df["country"] == "France"].iloc[:, 1:]

    # tracer
    plt.figure(figsize=(10, 5))
    plt.plot(years, country_campus.values.flatten(), label="Morocco", marker='o')
    plt.plot(years, country_other.values.flatten(), label="France", marker='x')
    plt.title("Population comparison: Morocco vs France")
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.legend()
    plt.tight_layout()
    plt.show()