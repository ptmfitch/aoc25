import csv

def print_grid(_robots, _w, _h, quadrants=False):
    poss = [x['pos'] for x in _robots]
    for i in range(_h):
        for j in range(_w):
            if quadrants and (j == int(w / 2) or i == int(h / 2)):
                print(' ', end='')
            elif [j, i] in poss:
                print(poss.count([j, i]), end='')
            else:
                print('.', end='')
        print()


csv_reader = csv.reader(open("inputs/14.csv"), delimiter=" ")

robots = []
w = 101
h = 103
secs = 100

for row in csv_reader:
    pos = [int(x) for x in row[0].split('=')[1].split(',')]
    vel = [int(x) for x in row[1].split('=')[1].split(',')]
    robots.append({'pos': pos, 'vel': vel})

print("Initial:")
print_grid(robots, w, h)
print()

def next_pos(pos, vel, _w, _h):
    return [(pos[0] + vel[0]) % _w, (pos[1] + vel[1]) % _h]

for i in range(secs):
    for robot in robots:
        robot['pos'] = next_pos(robot['pos'], robot['vel'], w, h)

print("After", secs, "seconds:")
print_grid(robots, w, h, True)
print()

def get_quadrant(x, y, mid_x, mid_y):
    # Top left
    if x < mid_x and y < mid_y:
        return 0
    # Top right
    elif x > mid_x and y < mid_y:
        return 1
    # Bottom left
    elif x < mid_x and y > mid_y:
        return 2
    # Bottom right
    elif x > mid_x and y > mid_y:
        return 3

def to_quadrants(_robots, _w, _h):
    mid_x = int(_w / 2)
    mid_y = int(_h / 2)
    quadrants = [0, 0, 0, 0]
    for robot in _robots:
        pos = robot['pos']
        if pos[0] == mid_x or pos[1] == mid_y:
            continue
        quadrants[get_quadrant(pos[0], pos[1], mid_x, mid_y)] += 1
    return quadrants

quadrants = to_quadrants(robots, w, h)

print("Quadrants:")
print(quadrants)
print()

def multiply_quadrants(_quadrants):
    return _quadrants[0] * _quadrants[1] * _quadrants[2] * _quadrants[3]

print("Quadrants multiplied:")
print(multiply_quadrants(quadrants))
print()

