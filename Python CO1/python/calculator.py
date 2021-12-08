num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
cal=(input("Enter your choice: \n\n+.Addition\n-.Subtraction\n*.Multiplication\n/.Division\n"))
if(cal=='+'):
    print("Sum of numbers: ",num1+num2)
elif(cal=='-'):
    print("Difference of numbers: ",num1-num2)
elif(cal=='*'):
    print("Product of numbers: ",num1*num2)
elif(cal=='/'):
    print("Quotient of numbers: ",num1/num2)
else:
    print("Invalid input")
