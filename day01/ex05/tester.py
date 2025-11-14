from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

# Charger l'image
array = ft_load("D:\\landscape.jpg")

# Afficher le tableau original
print("Original array:")
print(array)
print("Shape:", array.shape)
print("-" * 50)

# Appliquer les filtres et afficher les tableaux
filters = {
    "Inverted": ft_invert(array),
    "Red Filter": ft_red(array),
    "Green Filter": ft_green(array),
    "Blue Filter": ft_blue(array),
    "Grey Filter": ft_grey(array)
}
# Affichage des images (optionnel pour visualiser)
plt.figure(figsize=(15, 6))
plt.subplot(2, 3, 1)
plt.imshow(array)
plt.title("Original")
plt.axis("off")

for i, (name, arr) in enumerate(filters.items(), start=2):
    plt.subplot(2, 3, i)
    plt.imshow(arr)
    plt.title(name)
    plt.axis("off")

plt.tight_layout()
plt.show()
