def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return type(e).__name__
    except TypeError as t:
        return type(t).__name__

divide(5, 0)
divide(5, "0")

def getValue(list_or_map, index_or_key):
    try:
        return list_or_map[index_or_key]
    except IndexError as i:
        return type(i).__name__
    except KeyError as k:
        return type(k).__name__
    except TypeError as t:
        return type(t).__name__


getValue([1, 2, 3], 5)
getValue({"a": 1, "b": 2}, "c")
