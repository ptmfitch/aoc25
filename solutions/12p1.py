with open('inputs/12.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

farm = []
for line in lines:
    row = []
    for c in line.rstrip():
        row.append(c)
    farm.append(row)

print("Farm:")
[print(row) for row in farm]
print()

def expand_plot(plant, x, y, farm, edges, visited):
    next_plants = []
    for [dx, dy] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        i = x + dx
        j = y + dy
        if i >= 0 and i < len(farm) and j >= 0 and j < len(farm[i]):
            print("Checking", i, j, farm[i][j])
            if farm[i][j] == plant and (i, j) not in visited:
                print("Expanding to", i, j)
                next_plants.append([i, j])
            else:
                if (i, j) not in visited:
                    edges.add(((x, y), (i, j)))
        else:
            edges.add(((x, y), (i, j)))
    for [i, j] in next_plants:
        visited.add((i, j))
        expand_plot(plant, i, j, farm, edges, visited)
    return {
        "edges": edges,
        "visited": visited
    }

overall_visited = set()
plots = []
while len(overall_visited) < len(farm) * len(farm[0]):
    for i in range(0, len(farm)):
        for j in range(0, len(farm[i])):
            if (i, j) not in overall_visited:
                start_c = farm[i][j]
                start_x = i
                start_y = j
                edges = set()
                visited = set([(start_x, start_y)])
                plot = expand_plot(start_c, start_x, start_y, farm, edges, visited)
                print(plot)
                plots.append(plot)
                overall_visited = overall_visited.union(visited)

total = sum([len(x['edges']) * len(x['visited']) for x in plots])
print("Result:" , total)
