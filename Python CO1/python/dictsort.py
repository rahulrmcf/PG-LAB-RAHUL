import operator
d={"Rahul":1,"Amal":5,"Rafael":88}
print("Ordinary dictionary: ",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('Dictionary in ascending order by value',sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print('Dictionary in descending order by value',sorted_d)
