s=input("Enter the string: ")
print("The entered string is: ",s)
if(s.endswith("ing")):
    s=s+'ly'
else:
    s=s+'ing'
print("The output string: ",s)
