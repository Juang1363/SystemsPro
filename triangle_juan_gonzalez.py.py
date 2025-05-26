import math
class IsoscelesTriangle:
 def __init__(self, base, height):
    self.set_dimensions(base, height)
        
 def set_dimensions(self, base, height): #Here we are just setting dimesnions for the base and height. 
    #Also giving an error if the values are negative cuz negative values don't exist for triangles lol
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values.")
    self.__base = base
    self.__height = height
    self._recalculate_properties()

 def _recalculate_properties(self): #Here we are presenting the functions we want to use in our print all function
    self._calculate_side_length()
    self._calculate_perimeter()
    self._calculate_area()
    self._calculate_angles()

 def _calculate_side_length(self): #Here we are calcuating the side lengths by using math.sqrt from the math libray function and using the height and base like a regular iso triangle would.
    half_base = self.__base / 2
    self.side = math.sqrt(self.__height ** 2 + half_base ** 2)
#Perimeter and area are pretty self explanatory. Classic stuff learned in elementary lol
 def _calculate_perimeter(self):
    self.perimeter = self.__base + 2 * self.side

 def _calculate_area(self):
    self.area = (self.__base * self.__height) / 2

 def _calculate_angles(self): #Angles a bit more complicated but we use the method said in the lab notes and we ball forward.
        half_base = self.__base / 2
        self.alpha = math.degrees(math.atan(self.__height / half_base)) 
        self.beta = 180 - 2 * self.alpha
 def set_base(self, base): #These next two functions are done just in case we want to set the height and base to new properties.
    if base <= 0:
        raise ValueError("Base must be greater than 0.")
    self.__base = base
    self._recalculate_properties()

 def set_height(self, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0.")
    self.__height = height
    self._recalculate_properties()

 def print_all(self) -> None: #We print all of the functions now and they should work based on the test cases I did.
     print(f"------------------------------")
     print(f"base : {self.__base}")
     print(f"height : {self.__height}")
     print(f"side : {self.side}")
     print(f"perimeter: {self.perimeter}")
     print(f"area : {self.area}")
     print(f"alpha : {self.alpha}")
     print(f"beta : {self.beta}")
     print(f"------------------------------")
