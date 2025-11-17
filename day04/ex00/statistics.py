from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for key, value in kwargs.items():
        if value == "mean":
            if not args:
                print("ERROR")
                continue
            print("Mean =", sum(args)/len(args))
        elif value == "median":
            if not args:
                print("ERROR")
                continue
            print("Médiane =", sorted(args)[len(args)//2])
        elif value == "quartile":
            if not args:
                print("ERROR")
                continue
            q1 = sorted(args)[int(0.25 * len(args))]
            q3 = sorted(args)[int(0.75 * len(args))]
            print("quartile: ", [q1, q3])
        elif value == "var":
            if not args:
                print("ERROR")
                continue
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print("Variance:", variance)
        elif value == "std":
            if not args:
                print("ERROR")
                continue
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            std = variance ** 0.5
            print("Std:", std)
        else:
            continue
        