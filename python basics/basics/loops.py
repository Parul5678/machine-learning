i = 1
while i <= 5:
  print("hello")
  i += 1
print(i)

data = [2, 'navin', 4.5, 8, 'parul', 'python']

for value in range(10):
  print(value)

for value in range(10):
  if value % 3 == 0:
    continue
  print(value)

  for value in range(10):
    if value  == 5:
      break
    print(value)


#modules
from modules import add

result = modules.add()
print(result)