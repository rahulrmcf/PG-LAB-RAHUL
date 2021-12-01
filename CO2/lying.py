str=input("Enter a string:")
print("Inputed string is:",str)
if(str.endswith("ing")):
    str=str+'ly'
else:
        str=str+'ing'
print("The formated string is:",str)
