class person:
    varb=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("\nName: ",self.name,"\nAge: ",self.age)
p1=person("Rahul",24)
p2=person("Amal",22)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
p1.display()
p2.display()

print(person.varb)
print(p1.varb)
person.varb=person.varb+1
print(p1.varb)
print(person.varb)
p1.varb=20
print(p1.varb)
print(person.varb)
if(p1.age>p2.age):
    print(p1.name, "is elder")
else:
    print(p2.name,  "is elder")
