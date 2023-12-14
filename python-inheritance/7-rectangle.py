""" this is a definition """

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with given width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
        - A string representation.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# Example usage:
r = Rectangle(3, 5)
print(list(vars(r).keys()))
