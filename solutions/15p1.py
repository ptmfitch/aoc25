with open('inputs/15a.csv') as f:
    f.readline() # Skip the first line
    map = f.readlines()

with open('inputs/15b.csv') as f:
    f.readline() # Skip the first line
    instructions = f.readline()

robot = [0, 0]

for i in range(0, len(map)):
    line = map[i].rstrip()
    row = []
    for j in range(0, len(line)):
        c = line[j]
        if c == '@':
            robot = [i, j]
        row.append(c)
    map[i] = row

print("Map:")
[print(''.join(row)) for row in map]
print()

print("Robot:", robot)
print()

for i in range(0, len(instructions)):
    ins = instructions[i]
    print("Move {}:".format(ins))

    next_robot = robot.copy()
    if ins == '^':
        next_robot[0] -= 1
    elif ins == '>':
        next_robot[1] += 1
    elif ins == 'v':
        next_robot[0] += 1
    else:
        next_robot[1] -= 1

    next_obstacle = map[next_robot[0]][next_robot[1]]

    if next_obstacle == '.':
        map[next_robot[0]][next_robot[1]] = '@'
        map[robot[0]][robot[1]] = '.'
        robot = next_robot

    elif next_obstacle == 'O':
        if ins == '^':
            for j in range(next_robot[0], 0, -1):
                if map[j][next_robot[1]] == '.':
                    map[j][next_robot[1]] = 'O'
                    map[next_robot[0]][next_robot[1]] = '@'
                    map[robot[0]][robot[1]] = '.'
                    robot = next_robot
                    break
                elif map[j][next_robot[1]] == '#':
                    break
        elif ins == '>':
            for j in range(next_robot[1], len(map[0]) - 1):
                if map[next_robot[0]][j] == '.':
                    map[next_robot[0]][j] = 'O'
                    map[next_robot[0]][next_robot[1]] = '@'
                    map[robot[0]][robot[1]] = '.'
                    robot = next_robot
                    break
                elif map[next_robot[0]][j] == '#':
                    break
        elif ins == 'v':
            for j in range(next_robot[0], len(map) - 1):
                if map[j][next_robot[1]] == '.':
                    map[j][next_robot[1]] = 'O'
                    map[next_robot[0]][next_robot[1]] = '@'
                    map[robot[0]][robot[1]] = '.'
                    robot = next_robot
                    break
                elif map[j][next_robot[1]] == '#':
                    break
        else:
            for j in range(next_robot[1], 0, -1):
                if map[next_robot[0]][j] == '.':
                    map[next_robot[0]][j] = 'O'
                    map[next_robot[0]][next_robot[1]] = '@'
                    map[robot[0]][robot[1]] = '.'
                    robot = next_robot
                    break
                elif map[next_robot[0]][j] == '#':
                    break

    [print(''.join(row)) for row in map]
    print()

total = 0
for i in range(0, len(map)):
    line = map[i]
    for j in range(0, len(line)):
        if line[j] == 'O':
            total += i * 100 + j

print("Total:", total)