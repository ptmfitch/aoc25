with open('inputs/08.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

min_x = 0
min_y = 0
max_x = len(lines)
max_y = len(lines[0].rstrip())

print("Min x:", min_x)
print("Min y:", min_y)
print("Max x:", max_x)
print("Max y:", max_y)

frequencies = {}
nodes = []
antinodes = []
for i in range(0, len(lines)):
    line = lines[i].rstrip()
    for j in range(0, len(line)):
        char = line[j]
        if char != '.':
            if char in frequencies:
                frequencies[char].append([i, j])
                nodes.append([i, j])
            else:
                frequencies[char] = [[i, j]]
                nodes.append([i, j])

print("Frequencies ({}):".format(len(frequencies)))
for key in frequencies:
    print(key, frequencies[key])
    print()

print("Nodes ({}):".format(len(nodes)))
for node in nodes:
    print(node)
    print()


def antinode_is_valid(antinode):
    if antinode[0] < min_x or antinode[0] >= max_x:
        return False
    if antinode[1] < min_y or antinode[1] >= max_y:
        return False
    # if antinode in nodes:
    #     return False
    if antinode in antinodes:
        return False
    return True


for f in frequencies:
    ns = frequencies[f]
    for n in ns:
        for m in ns:
            if n != m:
                dx = m[0] - n[0]
                dy = m[1] - n[1]
                an = [n[0] - dx, n[1] - dy]
                if antinode_is_valid(an):
                    antinodes.append(an)

print("Antinodes:")
for antinode in antinodes:
    print(antinode)
    print()

print("Antinode count:", len(antinodes))
print()

for i in range(0, len(lines)):
    line = lines[i].rstrip()
    for j in range(0, len(line)):
        char = line[j]
        if [i, j] in antinodes:
            if char != '.':
                print('*', end='')
            else:
                print('#', end='')
        else:
            print(char, end='')
    print()
