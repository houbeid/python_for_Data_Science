from load_csv import load
import matplotlib.pyplot as plt


def aff_life(path: str):
    df = load(path)
    years = [int(col) for col in df.columns[1:]]
    life_expectancy = df[df["country"] == "Morocco"].iloc[:, 1:]

    plt.figure(figsize=(10, 5))

    plt.plot(years, life_expectancy.values.flatten(),
             label="Espérance de vie")
    plt.title("Morocco life expectancy projection")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()
