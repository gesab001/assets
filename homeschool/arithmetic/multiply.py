import random

numbers = [1,2,3,5,10]
for x in range(1,21):
    b = random.randint(0, 10)
    a = numbers[random.randint(0, len(numbers)-1)]
    print(str(x) + ".", str(a), "x", str(b))


