'''class Apple():
	def __init__(self, c, w, t, f):
		self.color = c 
		self.weight = w
		self.type = t
		self.freshness = f
		
	
	
	
apple = Apple("red", "16 oz", "Machintosh", "3 days old")

print(apple.color, apple.weight, apple.type, apple.freshness)
'''
import math 


class Circle():
	def __init__(self, d):
		self.diameter = int(d)
		
	def radius(self):
		return(self.diameter)/2 
		
		
	def area(self):
		return (self.radius())*(self.radius())* (math.pi)
		
	def change_diameter(self, d):
		self.diameter = int(d)
		

		
circle_1 = Circle(56)
print(circle_1.area())
print(math.pi)



print(circle_1.change_diameter(556))
print(circle_1.area())
