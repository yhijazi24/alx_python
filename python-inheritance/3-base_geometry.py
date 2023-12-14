""" this is a definition """
class BaseGeometry:
    def __repr__(self):
        return "<{} object at {}>".format(type(self).__name__, hex(id(self)))

