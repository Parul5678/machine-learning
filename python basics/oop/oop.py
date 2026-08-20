class computer:

  def config(self): #self refer to current object
    print("i7, 16GB, 1TB")

com1 = computer() #constructor
com2 = computer()

#computer.config(com1)
com1.config() #object becomes parameter