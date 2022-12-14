class Parent:
    def __init__(self, name):
        print('parent __init__', name)

class Parent2:
    def __init__(self, name):
        print('parent2 __init__', name)

class Child(Parent, Parent2):
    def __init__(self):
        print('child __init__')
        super().__init__('marceline')
       
child = Child()
print(Child.__mro__)