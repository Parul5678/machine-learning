class Laptop:
  def build(self):
    print("laptop build")

class Alien:
  def code(self, machine: Laptop):
    print("Alien building...")
    machine.build()

asus_rog = Laptop()
parul = Alien()
navin.code(asus_rog)