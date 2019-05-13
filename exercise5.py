import random

a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)

#Extra 1
ran_a = random.sample(range(100), 10)
ran_b = random.sample(range(100), 10)
ran_c = []
for i in ran_a:
    if i in ran_b and i not in ran_c:
        ran_c.append(i)

if not ran_c:
    print("The two lists have no common numbers!")
else:
    print(ran_c)

#Extra 2
print([i for i in set(a) if i in set(b)])