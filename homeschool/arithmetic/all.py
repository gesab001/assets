import random

for x in range(1,21):
    a = random.randint(10, 101)
    b = random.randint(0,9)
    print(str(x) + ".", str(a), "+", str(b))

print()
print()

for x in range(1,21):
    a = random.randint(10, 101)
    b = random.randint(0,9)
    print(str(x) + ".", str(a), "-", str(b))

print()
print()

numbers = [1,2,3,5,10]
for x in range(1,21):
    b = random.randint(0, 10)
    a = numbers[random.randint(0, len(numbers)-1)]
    print(str(x) + ".", str(a), "x", str(b))

print()
print()

for x in range(1,21):
    b = random.randint(0, 100)
    a = 0
    if (b%10==0): 
      a = 10
      print(str(x) + ".", str(b), "/", str(a))
    if(b%5==0):
      if(b>51):
          b = b%50
      a = 5
      print(str(x) + ".", str(b), "/", str(a))
    if(b%2==0):
      if (b>20):
         b = b%20 
      a = 2
      print(str(x) + ".", str(b), "/", str(a))
    if(b%3==0):
      if (b>30):
          
         b = b%30 
      a = 3
      print(str(x) + ".", str(b), "/", str(a))         
