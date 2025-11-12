import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        print ("the list are not the same size")
        return
    h = np.array(height)
    w = np.array(weight)
    if not np.issubdtype(h.dtype, np.number) or not np.issubdtype(w.dtype, np.number):
        print("the list are not int or float")
    bmi = w / (h ** 2)
    return (bmi.tolist())


def apply_limit (bmi: list[int | float], limit: int) -> list[bool]:
    bmi_limit = np.array(bmi)
    result = bmi_limit > limit
    return (result.tolist())
