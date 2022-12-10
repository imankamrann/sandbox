# class A:
#   name=""
#   def __init__(self):
#     print("I am from class A")
#   def m(self):
#     print("I am method from class A")

# class B(A):
#   def __init__(self):
#     super().__init__()
#     print("I am from class B")
#   def m(self):
#     super().m()
#     print("I am method from class B")

# class C(B):
#   def __init__(self):
#    super().__init__()
#    print("I am from class C")
#   def m(self):
#     super().m()
#     print("I am method from class C")

# class D(C):
#   def __init__(self):
#    super().__init__()
#    print("I am from class D")
#   def m(self):
#     super().m()
#     print("I am method from class D")

# #obj = A()
# obj= C()
# o=B()
# ob = A()

# print(type(obj)==type(ob))
# print(type(obj)==type(o))
# print(type(o)==type(ob))

class A:
  name=""
  def __init__(self):
    print("I am from class A")
  def m(self):
    print("I am method from class A")

class B(A):
    def __init__(self):
        print("I am from class B")
    def m(self):
        print("I am method from class B")

class C(A):
    pass
    # def __init__(self):
    #     super().__init__()
    #     print("I am from class C")
    # def m(self):
    #     print("I am method from class C")

class D(B,C):
    pass
    # def __init__(self):
    #     super().__init__()
    #     print("I am from class D")
    # def m(self):
    #     print("I am method from class D")



obj = D()

 




