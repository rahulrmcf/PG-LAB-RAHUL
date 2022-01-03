class solution:
    __private=0

    def sum(self):
        self.__private +=1
        print(self.__private)
obj=solution()
obj.sum()
obj.sum()
print(obj._solution__private)
