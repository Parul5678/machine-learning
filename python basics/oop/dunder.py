#double under __ (__init__)

class computer:

  brand = "AI"
  cpu = "i5" #class variable

  def __init__(self, cpu, ram, ssd): #self is first parameter
    print("init called")
    self.cpu = cpu
    self.ram = ram
    self.ssd = ssd

  def config(self): #self refer to current object
    print("config: ",self.cpu, self.ram, self.ssd)
  
  @classmethod
  def info(cls):
    return cls.brand
  
  @staticmethod
  def gb_to_bytes(gb):
    return gb * (1024 ** 3)


com1 = computer("i5", "16GB", "1TB") #constructor
com2 = computer("i9", "96GB", "2TB")

#com1.cpu = "i5"

#computer.config(com1)

#com1.config() #object becomes parameter
print(com1.cpu)
com1.config()
com2.config()
print(computer.info())
print(computer.gb_to_bytes(15))