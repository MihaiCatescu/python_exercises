'''
You live in the city of Perfectville where all roads are laid out in a perfect grid. The city provides its citizens with
a Walk Generating App on their phones -- every time you press the button it sends you an array of one-letter strings
representing the cardinal directions to walk (eg. ['N', 'S', 'W', 'E']). You always walk only a single block in a
direction and you know it takes you one minute to traverse one city block. Create a program where the user inserts the
number of minutes he has to spare (only even numbers) and receives the directions to walk (always returning to the
starting point).
'''

import random

walk_duration = int(input("How many minutes do you have to spare: "))
cardinal_points = ["N", "S", "E", "W"]
walk_directions = []


def get_directions():
    for i in range(1, walk_duration + 1):
        walk_directions.append(random.choice(cardinal_points))
    return walk_directions


def check_directions():
    if walk_directions.count('N') == walk_directions.count('S') and \
            walk_directions.count('E') == walk_directions.count('W'):
        return True
    else:
        return False


get_directions()


while check_directions() is False:
    walk_directions.clear()
    get_directions()
if True:
    print(walk_directions)
