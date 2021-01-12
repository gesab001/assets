import random

i = "a"
for x in range(1,101):
    a = random.randint(5, 10)
    b = random.randint(0,9)
    b = 5
    if (i=="a"):
      print(str(x) + ").", str(a), "+", str(b), "=", "____")
      print()
      i = "b"
    else:
      print(str(x) + ").", str(b), "+", str(a), "=", "____")
      print()
      i = "a"        

