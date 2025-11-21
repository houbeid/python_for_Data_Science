def callLimit(limit: int):
    count = 0  # compteur local à la closure

    def callLimiter(function):

        def limit_function(*args, **kwargs):
            nonlocal count  # permet de modifier "count" dans la closure

            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
