def greater_first(func):
  def wrap(a,b):
    if a<b:
      a,b = b,a
    return func(a,b)
  return wrap

@greater_first
def divide(a,b):
  if a<b:
    a,b = b,a
  return a/b

@greater_first
def sub(a,b):
  if a<b:
    a,b = b,a
  return a-b

result = divide(4,2)
print(result)

sub = greater_first(sub)