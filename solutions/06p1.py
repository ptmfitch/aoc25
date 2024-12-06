with open('inputs/06.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

lab = []
guard_x = 0
guard_y = 0
guard_dir = '^'
obstacles = []
visited = set()
for i in range(0, len(lines)):
    lab.append([])
    line = lines[i].strip()
    for j in range(0, len(line)):
        char = line[j]
        if char in ['^', 'v', '<', '>']:
            guard_x = i
            guard_y = j
            guard_dir = char
        elif char == '#':
            obstacles.append([i, j])
        lab[i].append(char)

print("Lab:")
for row in lab:
    print(row)
print()

print("Guard position: [{}, {}]".format(guard_x, guard_y))
print("Guard direction: {}".format(guard_dir))
print()

print("Obstacles: {}".format(obstacles))
print()

def next_pos(this_x, this_y, this_dir):
    if this_dir == '^':
        return [this_x - 1, this_y]
    elif this_dir == '>':
        return [this_x, this_y + 1]
    elif this_dir == 'v':
        return [this_x + 1, this_y]
    else:
        return [this_x, this_y - 1]

def turn_right(this_dir):
    if this_dir == '^':
        return '>'
    elif this_dir == '>':
        return 'v'
    elif this_dir == 'v':
        return '<'
    else:
        return '^'

while guard_x >= 0 and guard_x < len(lab) and guard_y >= 0 and guard_y < len(lab[0]):
    visited.add((guard_x, guard_y))
    print("Guard position: [{}, {}]".format(guard_x, guard_y))
    [next_x, next_y] = next_pos(guard_x, guard_y, guard_dir)
    if [next_x, next_y] in obstacles:
        guard_dir = turn_right(guard_dir)
        [next_x, next_y] = next_pos(guard_x, guard_y, guard_dir)
    else:
        guard_x = next_x
        guard_y = next_y

print(len(visited))
