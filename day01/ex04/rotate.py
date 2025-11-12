import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_Rotate(path: str, zoom_size: int) -> np.ndarray:
    try:
        pixels = ft_load(path)
        # Dimensions de l'image originale
        height, width = pixels.shape

        # Calcul du centre et du découpage pour zoom
        start_row = height//2 - zoom_size//2
        end_row   = height//2 + zoom_size//2
        start_col = width//2 - zoom_size//2
        end_col   = width//2 + zoom_size//2

        # Appliquer le slicing (zoom)
        pixels_zoom = pixels[start_row:end_row, start_col:end_col]
        # Ajouter un dernier axe pour obtenir (400, 400, 1)
        pixels_zoom_3d = pixels_zoom.reshape((zoom_size, zoom_size, 1))

        print("The shape of image is:", pixels_zoom_3d.shape, "or", pixels_zoom.shape)
        print(pixels_zoom_3d)

        # trouve la matrice transpose
        #pixels_transposed = np.transpose(pixels_zoom_3d, (1, 0, 2))
        pixels_transposed = pixels_zoom.T

        # # # Ajouter un dernier axe pour obtenir (400, 400, 1)
        # # pixels_transposed_3d = pixels_transposed.reshape((zoom_size, zoom_size, 1))

        print("New shape after Transpose:", pixels_transposed.shape)
        print(pixels_transposed)

        # Affichage de l'image zoomée
        plt.imshow(pixels_transposed.squeeze(), cmap="gray")  # .squeeze() supprime le dernier axe pour matplotlib
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("Zoomed Grayscale Image")
        plt.show()

        return pixels_transposed

    except Exception as e:
        print("Error:", str(e))
