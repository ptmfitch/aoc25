with open('inputs/09.txt') as f:
    input = f.readline().rstrip()

is_file = True
i = 0
c_id = 0
disk_map = []
free_spaces = []
files = []
for c in input:
    if is_file:
        for _ in range(0, int(c)):
            disk_map.append(str(c_id))
            files.append([str(c_id), i])
            i += 1
        c_id += 1
    else:
        for _ in range(0, int(c)):
            disk_map.append('.')
            free_spaces.append(i)
            i += 1
    is_file = not is_file

print(''.join(disk_map))
print()

print("Free spaces:", free_spaces)

print("Files:", files)
print()

for i in free_spaces:
    [f_id, f_i] = files.pop()
    if i > f_i:
        break
    disk_map[i] = f_id
    disk_map[f_i] = '.'
    if i % 100 == 0:
        print(''.join(disk_map))

checksum = 0
for i in range(0, len(disk_map)):
    id = disk_map[i]
    if id == '.':
        break
    checksum += (i * int(id))

print("Checksum:", checksum)

