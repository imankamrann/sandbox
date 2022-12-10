# class Student:
    
#     def setName(self, n):
#         self.__name = n
#     def getName(self):
#         return self.__name
        
#     def setMarks(self, m):
#         self.__marks = m
#     def getMarks(self):
#         return self.__marks
    
#     def  display(self):
#         print('Name: ', self.getName())
#         print('Marks: ', self.getMarks())
        
# S = Student()
# S.setName('John')
# S.setMarks(85.25)
# S.display()

class A:
    def init(self) -> None:
        self.multiply(15)
        print(self.i)
    def multiply(self, i):
        self.i =41

class B(A):
    def init(self) -> None:
        pass
        #super().init()
    def multiply(self,i):
        self.i=2*i

b=B()