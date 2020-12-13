import random

numbers = [5,10]
numberb = [1,2,5]
for x in range(1,21):
    b = numberb[random.randint(0, len(numberb)-1)]
    a = numbers[random.randint(0, len(numbers)-1)]
    print(str(x) + ".", str(a), "/", str(b))


