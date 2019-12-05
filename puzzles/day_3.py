
test_string = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
test_string2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

with open("../resources/input_day_3.txt") as file:
    wire_a = file.readline()
    wire_b = file.readline()

# a line has:
# start - int
# end - int
# direction - horizontal/vertical
# height - int

# all lines belonging to wire a
lines_a = []
# all lines belonging to wire b
lines_b = []
# all lines that intersect
crossing = []


# function generating a line
def gen_line(op: str, start: tuple):
    if op[0] == 'R':
        return [start, (start[0] + int(op[1:]), start[1]), 'hor', start[1]]
    if op[0] == 'U':
        return [start, (start[0], start[1] + int(op[1:])), 'ver', start[1] + int(op[1:])]
    if op[0] == 'D':
        return [start, (start[0], start[1] - int(op[1:])), 'ver', start[1] - int(op[1:])]
    if op[0] == 'L':
        return [start, (start[0] - int(op[1:]), start[1]), 'hor', start[1]]


# loop over all wire directions and populate lines_a & lines_b
start = (0, 0)
for s in wire_a.split(','):
    line = gen_line(s, start)
    lines_a.append(line)
    start = line[1]

start = (0, 0)
for s in wire_b.split(','):
    line = gen_line(s, start)
    lines_b.append(line)
    start = line[1]


# function for comparing line crossings, returning a list of line pairs that have intersections


# function for calculating the manhattan distance of each intersection point and returning the lowest

