class time:
    def __init__(self,hr,mins,sec):
        self.__hr=hr
        self.__mins=mins
        self.__sec=sec
    def __add__(self,a):
        h=self.__hr+a.__hr
        m=self.__mins+a.__mins
        s=self.__sec+a.__sec
        print(h,":",m,":",s)

print("Time 1")
h1=int(input("Enter hour: "))
m1=int(input("Enter minute: "))
s1=int(input("Enter second: "))
tm1=time(h1,m1,s1)
print("Time 2")
h2=int(input("Enter hour: "))
m2=int(input("Enter minute: "))
s2=int(input("Enter second: "))
tm2=time(h2,m2,s2)
tm1+tm2
