with open('inputs/12.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

farm = []
for line in lines:
    col = []
    for c in line.rstrip():
        col.append(c)
    farm.append(col)

print("Farm:")
[print(row) for row in farm]
print()

def expand_plot(plant, x, y, farm, edges, visited):
    next_plants = []
    for [dx, dy] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        i = x + dx
        j = y + dy
        if i >= 0 and i < len(farm) and j >= 0 and j < len(farm[i]):
            # print("Checking", i, j, farm[i][j])
            if farm[i][j] == plant and (i, j) not in visited:
                # print("Expanding to", i, j)
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
                # print(plot)
                plots.append(plot)
                overall_visited = overall_visited.union(visited)


def is_edge(plot, i, j):
    for edge in plot['edges']:
        if edge[1] == (i, j):
            return True
    return False


def edge_dir(edge):
    [a, b] = edge
    [x1, y1] = a
    [x2, y2] = b
    if x1 == x2:
        if y1 < y2:
            return 'R'
        else:
            return 'L'
    else:
        if x1 < x2:
            return 'D'
        else:
            return 'U'

sub_results = []
for i in range(0, len(plots)):
    plot = plots[i]
    print("Plot {}:".format(i))
    print()
    print("Visited:")
    [print(visit) for visit in plot['visited']]
    print()
    print("Edges:")
    [print(edge) for edge in plot['edges']]
    print()

    for i in range(-1, len(farm)+1):
        for j in range(-1, len(farm[0])+1):
            if (i, j) in plot['visited']:
                print('P', end='')
            elif is_edge(plot, i, j):
                print('E', end='')
            else:
                print('.', end='')
        print()
    print()

    edges = plot['edges']
    lines = []
    up_edges = sorted(filter(lambda x: edge_dir(x) == 'U', edges), key=lambda x: x[1][0])
    down_edges = sorted(filter(lambda x: edge_dir(x) == 'D', edges), key=lambda x: x[1][0])
    left_edges = sorted(filter(lambda x: edge_dir(x) == 'L', edges), key=lambda x: x[1][1])
    right_edges = sorted(filter(lambda x: edge_dir(x) == 'R', edges), key=lambda x: x[1][1])

    print("Up edges:")
    cols = set([x[1][0] for x in up_edges])
    sub_cols = []
    for col in cols:
        print("Row", col)
        sorted_col = sorted(filter(lambda x: x[1][0] == col, up_edges), key=lambda x: x[1][1])
        sub_col = []
        for i in range(0, len(sorted_col)):
            edge = sorted_col[i][1]
            next_edge = sorted_col[i+1][1] if i+1 < len(sorted_col) else None
            sub_col.append(edge)
            if not next_edge or edge[1] + 1 != next_edge[1]:
                sub_cols.append(sub_col)
                sub_col = []
    for sub_col in sub_cols:
        print(sub_col)
        lines.append(sub_col)
    print()
    print(len(lines))

    print("Down edges:")
    cols = set([x[1][0] for x in down_edges])
    sub_cols = []
    for col in cols:
        print("Row", col)
        sorted_col = sorted(filter(lambda x: x[1][0] == col, down_edges), key=lambda x: x[1][1])
        sub_col = []
        for i in range(0, len(sorted_col)):
            edge = sorted_col[i][1]
            next_edge = sorted_col[i+1][1] if i+1 < len(sorted_col) else None
            sub_col.append(edge)
            if not next_edge or edge[1] + 1 != next_edge[1]:
                sub_cols.append(sub_col)
                sub_col = []
    for sub_col in sub_cols:
        print(sub_col)
        lines.append(sub_col)
    print()
    print(len(lines))

    print("Left edges:")
    for edge in left_edges:
        print(edge)
    print()
    cols = set([x[1][1] for x in left_edges])
    sub_cols = []
    for col in cols:
        print("Col", col)
        sorted_col = sorted(filter(lambda x: x[1][1] == col, left_edges), key=lambda x: x[1][0])
        print([sorted_col[i][1] for i in range(0, len(sorted_col))])
        sub_col = []
        for i in range(0, len(sorted_col)):
            edge = sorted_col[i][1]
            next_edge = sorted_col[i+1][1] if i+1 < len(sorted_col) else None
            sub_col.append(edge)
            if not next_edge or edge[0] + 1 != next_edge[0]:
                sub_cols.append(sub_col)
                sub_col = []
    for sub_col in sub_cols:
        print(sub_col)
        lines.append(sub_col)
    print()
    print(len(lines))

    print("Right edges:")
    for edge in right_edges:
        print(edge)
    print()
    cols = set([x[1][1] for x in right_edges])
    sub_cols = []
    for col in cols:
        print("Col", col)
        sorted_col = sorted(filter(lambda x: x[1][1] == col, right_edges), key=lambda x: x[1][0])
        print([sorted_col[i][1] for i in range(0, len(sorted_col))])
        sub_col = []
        for i in range(0, len(sorted_col)):
            edge = sorted_col[i][1]
            next_edge = sorted_col[i+1][1] if i+1 < len(sorted_col) else None
            sub_col.append(edge)
            if not next_edge or edge[0] + 1 != next_edge[0]:
                sub_cols.append(sub_col)
                sub_col = []
    for sub_col in sub_cols:
        print(sub_col)
        lines.append(sub_col)
    print()
    print(len(lines))

    sub_results.append({'area': len(plot['visited']), 'lines': len(lines), 'product': len(plot['visited']) * len(lines)})

print("Sub results:")
print(sub_results)

total = sum([x['product'] for x in sub_results])
print("Result:" , total)
