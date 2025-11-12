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
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    Uses '-' as required.
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]  # R = 0
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]  # B = 0
    return green



def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    Uses '=' as required.
    """
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
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
