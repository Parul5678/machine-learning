class A:
  def __init__(self):
    print("in a init")

  def f1(self):
    print("f1 works")

  def f2(self):
    print("f2 works")

class B(A):
  def __init__(self):
    super()
    print("in b init")
    
  def f3(self):
    print("f3 works")

class C(A,B):
  def f4(Self):
    print("f4 works")

obj1 = A()
obj1.f1()

obj1 = B()
obj1.f1()

obj1 = C()
obj1.f1()

#every class in python is a child class 