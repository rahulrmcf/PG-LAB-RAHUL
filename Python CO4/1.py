class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        per=2*(self.length+self.breadth)
        return per
    def area(self):
        ar=(self.length*self.breadth)
        return ar
print("Enter the Length & Breadth of 1st rectangle")
l1=int(input("Length of rectangle: "))
b1=int(input("Breadth of rectangle: "))
p1=rectangle(l1,b1)
print("\nArea of 1st rectangle: ",p1.area())
print("Perimeter of 1st rectangle: ",p1.perimeter())
print("\nEnter the Length & Breadth of 2nd rectangle")
l2=int(input("Length of rectangle: "))
b2=int(input("Breadth of rectangle: "))
p2=rectangle(l2,b2)
print("\nArea of 2nd rectangle: ",p2.area())
print("Perimeter of 2nd rectangle: ",p2.perimeter())
if(p1.area()>p2.area()):
    print("\nArea of Rectangle 1 is greater")
elif(p2.area()>p1.area()):
    print("\nArea of Rectangle 2 is greater")
else:
    print("\nBoth are equal")
