'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen.
'''

counter_dict = {}

with open('names.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()


print(counter_dict)
