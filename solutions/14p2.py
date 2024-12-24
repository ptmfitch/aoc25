import csv

def print_grid(_robots, _w, _h, seconds):
    poss = [x['pos'] for x in _robots]
    grid = []
    max_robots_in_a_row = 0
    for i in range(_h):
        robots_in_a_row = 0
        line = []
        for j in range(_w):
            if robots_in_a_row > 10:
                if robots_in_a_row > max_robots_in_a_row:
                    max_robots_in_a_row = robots_in_a_row
            if [j, i] in poss:
                line.append('#')
                robots_in_a_row += 1
            else:
                line.append('.')
                robots_in_a_row = 0
        grid.append(line)
    if max_robots_in_a_row > 10:
        print("Seconds:", seconds)
        print('\n'.join([''.join(x) for x in grid]))


csv_reader = csv.reader(open("inputs/14.csv"), delimiter=" ")

robots = []
w = 101
h = 103

for row in csv_reader:
    pos = [int(x) for x in row[0].split('=')[1].split(',')]
    vel = [int(x) for x in row[1].split('=')[1].split(',')]
    robots.append({'pos': pos, 'vel': vel})

print("Initial:")
print_grid(robots, w, h, 0)
print()

def next_pos(pos, vel, _w, _h):
    return [(pos[0] + vel[0]) % _w, (pos[1] + vel[1]) % _h]

i = 1
while True:
    for robot in robots:
        robot['pos'] = next_pos(robot['pos'], robot['vel'], w, h)
    print_grid(robots, w, h, i)
    i += 1




