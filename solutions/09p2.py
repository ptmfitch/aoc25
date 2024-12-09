with open('inputs/09.txt') as f:
    input = f.readline().rstrip()

disk_map = []
c_id = 0
j = 0
spaces = []
files = []
for i in range(0, len(input)):
    l = int(input[i])
    if i % 2 == 0:
        for _ in range(0, l):
            disk_map.append(str(c_id))
        files.append([str(c_id), j, l])
        c_id += 1
    else:
        for _ in range(0, l):
            disk_map.append('.')
        spaces.append([j, l])
    j += l

print(''.join(disk_map))
print()

# print("Files: ", files)
# print("Spaces: ", spaces)
# print()

def first_available_space(f_l, f_i):
    for i in range(0, len(spaces)):
        space = spaces[i]
        if space[0] < f_i and space[1] >= f_l:
            return i
    return -1

try:
    while True:
        [f_id, f_i, f_l] = files.pop()
        i = first_available_space(f_l, f_i)
        if i > -1:
            [s_i, s_l] = spaces.pop(i)
            for i in range(0, f_l):
                disk_map[s_i + i] = f_id
            for i in range(0, f_l):
                disk_map[f_i + i] = '.'
            if f_l != s_l:
                spaces = spaces[:i] + [[s_i + f_l, s_l - f_l]] + spaces[i:]
                spaces.sort()
            # print(''.join(disk_map))
except IndexError:
    pass

checksum = 0
for i in range(0, len(disk_map)):
    id = disk_map[i]
    if id != '.':
        checksum += (i * int(id))

print("Checksum:", checksum)
