a = 5
b = 6

# c = a + b
c = int.__add__(a, b)

print(c)
print(a.__str__())  # String method which returns the value of the object


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} : {self.balance}'

    def __add__(self, other):
        return Account('combined', self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance


user1 = Account('parul', 2000)
user2 = Account('kiran', 5332)

combine = user1 + user2

print(user1)
print(user2)
print(combine)

if user1 > user2:
    print("parul pays the bill")
else:
    print("kiran pays the bill")


