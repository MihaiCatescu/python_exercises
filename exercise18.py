'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen.
'''

with open('names.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        print(line)
        line = open_file.readline()

for elem in line:
    if elem == 0:
        ele