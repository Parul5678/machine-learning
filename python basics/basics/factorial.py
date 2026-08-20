import sys
from time import sleep
sys.getrecursionlimit()
sys.setrecursionlimit(100)
def fact(num):
  res = 1

  for i in range(1, num+1):
    res = res*i

  return res 

result = fact(5)
print(result)

#recursion
count = 1
def greet():
  global count
  print("hello", count)
  count += 1
  sleep(0.02)
  greet()

greet()

#using recursion in factorial 
def fact(num):
  if num == 1:
    return 1

  return num * fact(num-1)

result = fact(5)
print(result)
