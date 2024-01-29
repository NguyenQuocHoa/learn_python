# https://v1study.com/python-bai-tap-bai-tap-phan-class.html
import math
# Class Name    : Point
# Note          : Class point in flat 2D
# Created       : 2024/01/29
# Modified      :
class Point:
    _position_x = 0
    _position_y = 0

    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Param         : position_x
    # Param         : position_y
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self, position_x, position_y):
        self._position_x = position_x
        self._position_y = position_y

    # Function Name : __str__
    # Note          : print stringify of instance
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __str__(self):
        return "Position is({}, {})".format(self._position_x, self._position_y)


# Class Name    : Ellipse
# Note          : Class ellipse in flat 2D
# Created       : 2024/01/29
# Modified      :
class Ellipse(Point):
    _width = 0
    _height = 0

    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Param         : position_x
    # Param         : position_y
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self, position_x, position_y, width, height):
        super().__init__(position_x, position_y)
        self._width = width
        self._height = height

    # Function Name : calc_area_ellipse
    # Note          : calculate area of ellipse
    # Param         : self
    # Return        : area ellipse
    # Created       : 2024/01/29
    # Modified      :
    def calc_area_ellipse(self):
        return math.pi * self._width / 2 * self._height / 2
    
    # Function Name : __str__
    # Note          : print stringify of instance
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __str__(self):
        return ("Position is({}, {}) and width = {}, height = {}"
                .format(self._position_x, self._position_y, self._width, self._height))


# Class Name    : Ellipse
# Note          : Class ellipse in flat 2D
# Created       : 2024/01/29
# Modified      :
class Circle(Ellipse):
    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Param         : position_x
    # Param         : position_y
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self, position_x, position_y, radius):
        width = radius * 2
        super().__init__(position_x, position_y, width, width)

    # Function Name : calc_area_circle
    # Note          : calculate area of circle
    # Param         : self
    # Return        : area circle
    # Created       : 2024/01/29
    # Modified      :
    def calc_area_circle(self):
        return super().calc_area_ellipse()
    
    # Function Name : __str__
    # Note          : print stringify of instance
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __str__(self):
        return ("Position is({}, {}) and radius = {}"
                .format(self._position_x, self._position_y, self._width / 2))

# Check results
# Point class
print("=================> Point <===============")
position_x = float(input("Type position x: "))
position_y = float(input("Type position y: "))
point = Point(position_x, position_y)
print(point)
print("=================> Point <===============\n")

# Ellipse class
print("=================> Ellipse <===============")
width = float(input("Type ellipse width: "))
height = float(input("Type ellipse height: "))
ellipse = Ellipse(position_x, position_y, width, height)
print(ellipse)
print("Area of ellipse is: {}".format(ellipse.calc_area_ellipse()))
print("=================> Ellipse <===============\n")

# Circle class
print("=================> Circle <===============")
radius = float(input("Type circle radius: "))
circle = Circle(position_x, position_y, radius)
print(circle)
print("Area of circle is: {}".format(circle.calc_area_circle()))
print("=================> Circle <===============\n")

