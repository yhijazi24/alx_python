""" this is a definition """
def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class
    that inherited from the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
