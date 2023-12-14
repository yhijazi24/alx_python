""" this is a definition """
class BaseGeometry:
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a class that inherited from a_class, otherwise False."""
    def __repr__(self):

        return "<{} object at {}>".format(type(self).__name__, hex(id(self)))

