a = int(input("a: "))
b = int(input("b: "))
result = a/b
try:
  print("result", result)

except ZeroDivisionError:
  print("error duw to division by 0")
except ValueError:
  print("value error")
except Exception:
  print("exception")


finally:
  print("execute all")

print("end of execution")

class hello(thread):
  def run(self):
    print(a)
    sleep(0.3)
