class Student:
    def setName(self, n):
        self.__name = n

    def getName(self):
        return self.__name

    def display(self):
        print("name: ", self.__name)

S = Student()
S.setName("marceline")
S.display()
