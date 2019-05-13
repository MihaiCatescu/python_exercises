import random

list_a = random.sample(range(100), 10)
list_b = random.sample(range(100), 15)
list_c = []

for i in list_a:
    if i in list_b and i not in list_c:
        list_c.append(i)

if not list_c:
    print("The two lists have no common numbers.")
else:
    print(list_c)