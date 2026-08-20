import math as m # importing the module
from math import sqrt, ceil, pow
print('hello')

def add(x,y):
  a = x
  b = y
  c = a + b
  return c
  
result = add(2,5)
result = add(10,20)
# grouping of related functions of one thing into a module

num = 25
result = sqrt(num)
result1 = m.ceil(59.4)
result2 = pow(5,3)
print(result)
print(result1)
print(result2)

def subt(num1, *num2): #variable length arguements
  return num1 - num2

def person(name, **age): # to pass multiple values
  print(name)
  print(age)

person('parul', 19)

a = 10
def something():
  #print(globals()) #to print global variables
  globals()['a'] = 20

  a = 15 #local variable

print(a)

#higher order function(functional programming)

def square(num):
  return num * num
def cube(num):
  return num*num*num

def operate(nums, operation):
  for i in nums:
    result = operation(i)
    print(result)

num = [3,5,7]
operate(num, square)

#anonymous function
#def fun(num):
 # return num*num

fun = lambda num: num*num

result = fun(5)
print(result)

#filter function in python 
from functools import reduce
nums = [4,2,9,7,5,1,6,8]
evens = []
 
evens = list(filter(lambda n : n%2==0, nums)) #pass function and iterable
doubles = list(map(lambda n : n*2 ,evens))
sum = reduce(lambda a,b: a+b ,doubles)

print(evens)

#inner function
def outer():
  print("outer function")
  def inner ():
    print("inner function")
  #inner()
  return inner

something = outer()
print(something)
