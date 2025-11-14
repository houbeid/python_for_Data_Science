from load_csv import load
import matplotlib.pyplot as plt


def projection_life(path_expectancy: str, path_adjusted: str):
    df_expectancy = load(path_expectancy)
    df_adjusted = load(path_adjusted)
    life_expectancy = df_expectancy["1900"]
    gross_product = df_adjusted["1900"]

    # tracer
    plt.figure(figsize=(10, 5))
    plt.scatter(gross_product, life_expectancy)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.tight_layout()
    plt.show()
