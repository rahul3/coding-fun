"""Methods commonly used by me"""

def dict_lval(dct: dict) -> float:
    """Gets the key with lowest value in a dict of key, value pairs

    Args:
        dct (dict): Dictionary to look in

    Returns:
        Lowest value in the dictionary
    """
    return min(dct, key=dct.get)

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))