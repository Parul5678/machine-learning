from abc import ABC, abstractmethod

#class A(ABC):

#  @abstractmethod
 # def show(self):
   # pass

#obj1 = A()
#bj1.show()
class PaymentGateway(ABC):
  @abstractmethod
  def pay(self):
    pass


class RazorPay(PaymentGateway):
  def pay(self):
    print("pay using razorpay..")

class Purchase():

  def __init__(self, gateway):
    self.gateway = gateway

  def checkout(self):
    print("checking out..")

    self.gateway.pay()

gateway1 = RazorPay()
purchase = Purchase(gateway1)

purchase.checkout()