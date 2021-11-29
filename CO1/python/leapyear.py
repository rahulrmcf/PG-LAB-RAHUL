s=int(input("Enter the start year: "))
e=int(input("Enter the end year:"))
if(s<e):
    print("Leap years are:",end=" ")
for i in range(s,e):
    if i%4==0 and i%100!=0:
            print(i,end=" ")
