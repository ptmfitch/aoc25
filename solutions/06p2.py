with open('inputs/06.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

lab = []
guard_x = 0
guard_y = 0
guard_dir = '^'
obstacles = []

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

start_lab = lab.copy()
start_guard_x = guard_x
start_guard_y = guard_y
start_guard_dir = guard_dir
start_obstacles = obstacles.copy()

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

def turn_left(this_dir):
    if this_dir == '^':
        return '<'
    elif this_dir == '>':
        return '^'
    elif this_dir == 'v':
        return '>'
    else:
        return 'v'

infinite_loops = set()
for i in range(0, len(lab)):
    if i % 10 == 0:
        print("Checking row {}/{}".format(i, len(lab)))
    for j in range(0, len(lab[i])):
        # if j % 10 == 0:
        #     print("Checking column {}".format(j))
        if [i, j] in obstacles:
            # print("Obstacle already exists at [{}, {}]".format(i, j))
            continue
        else:
            lab = start_lab.copy()
            guard_x = start_guard_x
            guard_y = start_guard_y
            guard_dir = start_guard_dir
            obstacles = start_obstacles.copy()
            visited = set()

            # print("Adding new obstacle at [{}, {}]".format(i, j))
            temp_obstacles = obstacles.copy()
            temp_obstacles.append([i, j])
            while guard_x >= 0 and guard_x < len(lab) and guard_y >= 0 and guard_y < len(lab[0]):
                [start_x, start_y, start_dir] = [guard_x, guard_y, guard_dir]
                [next_x, next_y] = next_pos(guard_x, guard_y, guard_dir)
                if [next_x, next_y] in temp_obstacles:
                    guard_dir = turn_right(guard_dir)
                    [next_x, next_y] = next_pos(guard_x, guard_y, guard_dir)
                else:
                    guard_x = next_x
                    guard_y = next_y

                if (start_x, start_y, start_dir) in visited or start_dir != guard_dir and (start_x, start_y, guard_dir) in visited:
                    # print("Infinite loop detected with new obstacle at [{}, {}]".format(i, j))
                    infinite_loops.add((i, j))
                    break
                visited.add((start_x, start_y, start_dir))
            # print("Exited lab at [{}, {}]".format(guard_x, guard_y))

print(len(infinite_loops))
