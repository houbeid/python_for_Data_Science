


# def NULL_not_found(object: any) -> int:
#     if object is None:
#         print ("Nothing: {object} ", type(object))
#     elif isinstance(object, float) and object != object:
#         print ("Cheese: {object} ", type(object))
#     elif object == 0:
#         print ("Zero: {object} ", type(object))
#     elif object == "":
#         print ("Empty: {object} ", type(object))
#     elif object is False:
#         print ("Fake: {object} ", type(object))
#     return 1

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0

