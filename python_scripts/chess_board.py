class Space:
	left_right = ["A", "B", "C", "D", "E", "F", "G", "H"]
	bot_top = ["1", "2", "3", "4", "5", "6", "7", "8"]
	
	def __init__(self, h, v):
		self.hoz_pos = h 
		self.ver_pos = v 
	def __repr__(self):
		v = self.left_right[self.hoz_pos] + " " + \
		self.bot_top[self.ver_pos]
		return v 
		
		
class Board:
	def __init__(self):
		self.spaces = []
	
		for i in range(8):
			for j in range(8):
				space_name = Space(i, j)
				self.spaces.append(space_name)
	
		

		
		
	def __repr__(self):
		v = "\
		{}"
		
		v = v.format(self.spaces)
		return v 
				
				
board = Board()

print board





				
				
		
		 