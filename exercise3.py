a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)

#Extra 2
# b = [i for i in a if i < 5]

#Extra 3
num = int(input("Give me a number: "))
c = []
for i in a:
    if i < num:
        c.append(i)
print(c)