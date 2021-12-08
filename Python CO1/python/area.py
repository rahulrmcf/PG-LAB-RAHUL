c=int(input("Enter your choice: \n\n1.Area of Circle\n2.Area of rectangle\n3.Area of square\n\n"))
if(c==1):
    r=int(input("Enter the radius of the circle: "))
    print("Area of circle",3.14*r*r)
elif(c==2):
    l=int(input("Enter the length of the rectangle: "))
    b=int(input("Enter the breadth of the rectangle: "))
    print("Area of rectangle",l*b)
elif(c==3):
    a=int(input("Enter the side of a square: "))
    print("Area of square",a*a)
else:
    print("Invalid input")
    
