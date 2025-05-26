class mcomplex:
	def __init__(self, r: int, i: int):
		"""
		Initialize a mcomplex object and its data attributes
		"""
		self.__update(r, i)	
	def __update(self, r: int = 0, i: int = 0):
		"""
		Update the data attributes of this mcomplex object. (Private method)
		Must include real part, imaginary part and the distance magnitude.
		"""
		self.r = r
		self.i = i

	def print(self):
		print(f"{self.r} + {self.i}i")

	def __add__(self, other) -> 'mcomplex':
		"""
	    :return: (a + bi) + (c + di) = (a + c) + (b + d)i
		"""
		a=self.r
		b=self.i    
		c=other.r
		d=other.i
        
		
		
		equation=mcomplex(a+c,b+d)
		return equation 

	def __sub__(self, other) -> 'mcomplex':
		"""
		Calculate and return the substraction of two mcomplex objects.
		:return: (a + bi) - (c + di) = (a - c) + (b - d)i
		"""
    	
		a=self.r
		b=self.i    
		c=other.r
		d=other.i 
		equation2=mcomplex(a-c,b-d)
		return equation2   

	def __mul__(self, other) -> 'mcomplex':
		"""
		Calculate and return the multiplication of two mcomplex objects.
		:return: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
		"""
        
		a=self.r
		b=self.i    
		c=other.r
		d=other.i
		equation3=mcomplex(a*c-b*d,a*d+b*c)
		return equation3

	def __truediv__(self, other) -> 'mcomplex':
		"""
		Calculate and return the division of two mcomplex objects.

		:return: (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
		"""
		a=self.r
		b=self.i    
		c=other.r
		d=other.i
        
		denominator = c**2 + d**2
		if denominator == 0:
            
			raise ZeroDivisionError("Cannot divide by zero complex number")
		real_part = (a * c + b * d) / denominator
		imaginary_part = (b * c - a * d) / denominator
		equation4= mcomplex(real_part, imaginary_part)
		return equation4





	def __eq__(self, other) -> bool:
		"""
		Compare whether two mcomplex objects are equal. 
		Return True if both mcomplex objects are the same, False otherwise.
		"""
		return self.r == other.r and self.i == other.i


	def __ne__(self, other) -> bool:
		"""
		Compare whether two mcomplex objects are not equal. 
		Return True if both mcomplex objects are not the same, False otherwise.
		"""
		return self.r != other.r and self.i != other.i


	def __lt__(self, other) -> bool:
		"""
		Calculate whether the first mcomplex number is less than the second one and return True,
		otherwise return False.
		:return: self < other ?
		"""
		return (self.r**2 + self.i**2) < (other.r**2 + other.i**2)


	def __gt__(self, other) -> bool:
		"""
		Calculate whether the first mcomplex number is greater than the second one and return True,
		otherwise return False.
		:return: self > other ?
		"""
		
		return (self.r**2 + self.i**2) > (other.r**2 + other.i**2)

def test():
	# Any test code that you would like to run
	x = mcomplex(1, 2)
    
	y = mcomplex(2, 4)
    
	z = x + y
    
	z.print()

    
	z = x - y
        
	z.print()

    
	z = x * y
        
	z.print()

    
	z = x / y
    
	z.print()

    
	print(x == y)
    
	print(x != y)
    
	print(x < y)

    
	print(x > y)


	return

if __name__ == "__main__":
	test()