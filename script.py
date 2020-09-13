from random import randint
from statistics import mean

mean_random = []
for i in range(1,1000):
    array_number = []
    for i in range(0,100):
        array_number.append(randint(0,100))
    mean_random.append(mean(array_number))

print(mean(mean_random))