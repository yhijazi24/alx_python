""" this is a definition """
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a class that inherited from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)
