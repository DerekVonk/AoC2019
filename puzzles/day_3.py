from enum import Enum
from functools import reduce

test_string = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
test_string2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

with open("../resources/input_day_3.txt") as file:
    wire_a = file.readline()
    wire_b = file.readline()


# a line has:
# start (x or y) - int
# end (x or y) - int
# direction - horizontal/vertical
# opposite_coordinate - int
class Direction(Enum):
    H = 'horizontal'
    V = 'vertical'


# all lines belonging to wire a
lines_a = []
# all lines belonging to wire b
lines_b = []
# all lines that intersect
crossing = []


# function generating a line
def gen_line(op: str, start_coor: list):
    x = 0
    y = 1
    if op[0] == 'R':
        # calculate new x-coordinate
        new_x = start_coor[x] + int(op[1:])
        # create line properties [start x, end x, 'hor', opposite coordinate = y]
        ln = [start_coor[x], new_x, Direction.H, start_coor[y]]
        # set new start coordinate
        new_c = [new_x, start_coor[y]]
        return ln, new_c
    if op[0] == 'L':
        # calculate new x-coordinate
        new_x = start_coor[x] - int(op[1:])
        # create line properties [start x, end x, 'hor', opposite coordinate = y]
        ln = [start_coor[x], new_x, Direction.H, start_coor[y]]
        # set new start coordinate
        new_c = [new_x, start_coor[y]]
        return ln, new_c
    if op[0] == 'U':
        # calculate new y-coordinate
        new_y = start_coor[y] + int(op[1:])
        # create line properties [start y, end y, 'hor', opposite coordinate = x]
        ln = [start_coor[y], new_y, Direction.V, start_coor[x]]
        # set new start coordinate
        new_c = [start_coor[x], new_y]
        return ln, new_c
    if op[0] == 'D':
        # calculate new y-coordinate
        new_y = start_coor[y] - int(op[1:])
        # create line properties [start y, end y, 'hor', opposite coordinate = x]
        ln = [start_coor[y], new_y, Direction.V, start_coor[x]]
        # set new start coordinate
        new_c = [start_coor[x], new_y]
        return ln, new_c


# loop over all wire directions and populate lines_a & lines_b
start_a = [0, 0]
for s in wire_a.split(','):
    line, new_coor = gen_line(s, start_a)
    lines_a.append(line)
    start_a = new_coor

start_b = [0, 0]
for s in wire_b.split(','):
    line, new_coor = gen_line(s, start_b)
    lines_b.append(line)
    start_b = new_coor


# function for comparing line crossings, returning a list of line pairs that have intersections
for l_a in lines_a:
    for l_b in lines_b:
        if l_a[2] != l_b[2]:
            if (l_a[0] < l_b[3] < l_a[1] or l_a[1] < l_b[3] < l_a[0]) and (l_b[0] < l_a[3] < l_b[1] or l_a[1] < l_b[3] < l_a[0]):
                print(f'found crossing lines on x: {l_a[3]} and y: {l_b[3]}')
                print(f'line_a = {l_a}')
                print(f'line_b = {l_b}\n')
                crossing.append((l_a[3], l_b[3]))


# map all coordinates to absolute values to calculate manhattan distance
crossing = [(abs(i[0]), abs(i[1])) for i in crossing]
# function for calculating the manhattan distance of each intersection point and returning the lowest
closest_coordinate = reduce(lambda a, b: a if sum(a) < sum(b) else b, crossing)

print(f"1. lowest manhattan distance is", sum(closest_coordinate))
