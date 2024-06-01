# spcl function that gets involved everytime an object is created for thr class

# Syntax
# class className:
#     def __init__ (self, param1, param2,..):
#         #initialize instance variables

class rectangle:
    def __init__(self,height,width):
        print(f"rectangle created with a constructor with height {height} and width {width}")
        self.height= height
        self.width= width

    def dimensions(self, height, width):
        self.height= height
        self.width= width

    def area(self):
        return self.height*self.width
    
rectangle1= rectangle(4,3)
rectangle1.dimensions(4,3)
print("height and width:", rectangle1.height, rectangle1.width)
print("area", rectangle1.area())
