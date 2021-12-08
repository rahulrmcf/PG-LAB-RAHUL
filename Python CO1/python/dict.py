import  operator
d1= {"Rahul":23,"Arun":5}
d2={"Ananthu":151,"Sooraj":2}
print("Dictionary 1:",d1)
print("Dictionary 2:",d2)
d=d1.copy()
d.update(d2)
print("Merged Dictionary: ",d)
