with open('inputs/10.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

_map = []
trail_heads = []
for i in range(0, len(lines)):
    line = lines[i].rstrip()
    row = []
    for j in range(0, len(line)):
        c = line[j]
        row.append(c)
        if c == '0':
            trail_heads.append([i, j])
    _map.append(row)

print("Map:")
for row in _map:
    print(row)
    print()

print("Trail heads ({}):".format(len(trail_heads)))
print(trail_heads)
print()


def recurse(x, y, h, m, v, ss):
    print("Visiting", x, y, h)
    for [i, j] in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]):
            c = m[i][j]
            if c != '.':
                nh = int(c)
                if nh == h+1:
                    if nh == 9:
                        print("Found a path!")
                        ss.add((i, j))
                    elif [i, j] not in v:
                        v.append([x, y])
                        recurse(i, j, h+1, m, v.copy(), ss)


scores = []
for trail_head in trail_heads:
    [start_x, start_y] = trail_head
    visited = [trail_head]
    height = 0
    score = set()
    recurse(start_x, start_y, height, _map, visited.copy(), score)
    print("Score:", score)
    scores.append(len(score))

print("Scores ({}):".format(len(scores)))
print(scores)

print("Total score:", sum(scores))
