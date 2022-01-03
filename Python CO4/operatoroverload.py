class jerin:
    def __init__(self,h):
        self.__h=h

    def __add__(self,a):
        print(self.__h+a.__h)

    def __lt__(self,a):
        if(self.__h<a.__h):
            return(True)
    def __gt__(self,a):
        if(self.__h>a.__h):
            return(True)
    def __eq__(self,a):
        if(self.__h==a.__h):
            return(True)
a1=jerin(10)
a2=jerin(20)
a1+a2
if(a1<a2):
    print("a1 is smaller")
else:
    print("a2 is smaler")   

if(a1>a2):
    print("a1 is greater")
else:
    print("a2 is greater")

if(a1==a2):
    print("Both are equal")
else:
    print("Both are not equal")
