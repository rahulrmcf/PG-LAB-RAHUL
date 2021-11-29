l=[3,4,5,78]
x=int(input("Enter the element to search:"))
for i in l:
    if x==i:
        print("Element found in the list")
        break
else:
    print("Element not found")
