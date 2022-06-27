# length = int(input("Input the length: "))
# width = int(input("Input the width: "))
# def area(length,width):
#     area1 = length * width
#     print(area1)
# area(length,width)

# alternatively

class Area(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        area1 = self.length * self.width
        return area1 #or 
       
    def printArea(self):
        print(self.length * self.width)
        
    def printPerimeter(self):
        print(2*self.length + 2*self.width)
        
a = Area(4,5)
a.printArea()
a.printPerimeter()
a.area()