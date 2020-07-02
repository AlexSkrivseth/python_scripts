# Wall Framer Program




class Wall():
    def __init__(self, wall_thickness=5.5, wall_height=96, wall_length=0, stud_layout=16, plate_number=3):
        self.wall_thickness = wall_thickness
        self.wall_height = wall_height
        self.wall_length = wall_length
        self.plate_number = plate_number
        self.stud_layout = stud_layout
        self.plate_thickness = self.plate_number * 1.5
        self.stud_length = self.wall_height - self.plate_thickness
        self.stud_number = (self.wall_length / self.stud_layout) + 1
        self.windows = None # add a window class
        self.doors = None # add a door class
        self.interior_finish = None # add an interior_finish class
        self.exterior_sheeting = None # add an exterior_sheeting class
        self.siding = None # add a siding class

    def __repr__(self):
        return "This wall will need {} studs cut at {} inches".format(self.stud_number, self.stud_length)
    def __str__(self):
        return "This wall will need {} studs cut at {} inches".format(self.stud_number, self.stud_length)





wall_length = int(input("what is the length of the wall in inches? : "))

wall1 = Wall(wall_length=wall_length)
print(wall1)
