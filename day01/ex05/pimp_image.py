import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image.
    Example: white becomes black, red becomes cyan, etc.
    """
    invert = 255 - array
    return invert


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel.
    Uses '*' as required.
    """
    red = array * [1, 0, 0]
    print("Red Filter array:")
    print("The shape of image is", red.shape)
    print(red)
    print("-" * 50)
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    Uses '-' as required.
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]  # R = 0
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]  # B = 0
    print("green Filter array:")
    print("The shape of image is", green.shape)
    print(green)
    print("-" * 50)
    return green



def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    Uses '=' as required.
    """
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    print("blue Filter array:")
    print("The shape of image is", blue.shape)
    print(blue)
    print("-" * 50)
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts image to grayscale (average of R, G, B).
    Uses '/' as required.
    """
    grey = array.copy()
    grey = (grey[:, :, 0] / 3 + grey[:, :, 1] / 3 + grey[:, :, 2] / 3)
    grey = grey.astype(np.uint8)
    return np.stack((grey, grey, grey), axis=2)
