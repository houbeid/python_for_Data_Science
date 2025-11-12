from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:

    if not path.lower().endswith(".jpg") and not path.lower().endswith(".jpeg"):
        print ("Error: Only JPG/JPEG images are supported.")
        return 
    img = Image.open(path)
    img = img.convert("RGB")
    pixel = np.array(img)
    print("The shape of image is: ", pixel.shape)
    return pixel
