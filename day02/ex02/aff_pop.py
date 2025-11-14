from load_csv import load
import matplotlib.pyplot as plt

def str_to_int(value):
    if isinstance(value, str):
        value = value.strip()
        if value.endswith("M"):
            return float(value[:-1]) * 1_000_000
        elif value.endswith("K"):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    elif pd.isna(value):
        return 0
    else:
        return float(value)

def aff_pop(path: str) :
    df = load(path)
    # convertir les colonnes "années" en int
    years = [str(y) for y in range(1800, 2051)]  # 2051 car upper bound non inclus
   # years = [int(col) for col in years]
    country_campus = df[df["country"] == "Morocco"][years]
    country_other = df[df["country"] == "France"][years]
    country_campus = country_campus.applymap(str_to_int)
    country_other = country_other.applymap(str_to_int)
    years_int = [int(y) for y in years]

    # tracer
    plt.figure(figsize=(10, 5))
    plt.plot(years_int, country_campus.values.flatten(), label="Morocco")
    plt.plot(years_int, country_other.values.flatten(), label="France")
    plt.title("Population comparison: Morocco vs France")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    plt.show()