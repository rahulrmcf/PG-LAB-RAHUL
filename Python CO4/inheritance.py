class student:
    def getstudent(self,rollno,name,cour,rank):
        self.roll=rollno
        self.name=name
        self.cour=cour
        self.rank=rank
    def displaystudent(self):
        print("Roll Number: ",self.roll)
        print("Name: ",self.name)
        print("Course: ",self.cour)
        print("Rank: ",self.rank)

class test(student):
    def getmarks(self,m):
        self.mark=m
    def displaymarks(self):
        print("Mark :",self.mark)

s=test()
s.getstudent(1,"Abirami","MCAR&L",1)
s.getmarks(100)
s.displaystudent()
s.displaymarks()
