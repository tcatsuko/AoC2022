import networkx as nx
f = open('aoc12.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# build the 2D map
elmap = []
for line in raw_input:
    elmap += [[x for x in line]]
print()
G = nx.DiGraph()
rows = len(elmap)
cols = len(elmap[0])
lowest_elevations = []
for y in range(rows):
    for x in range(cols):
        # get current position
        current_pos = (x, y)
        current_elevation = elmap[y][x]
        if current_elevation == 'S':
            current_elevation = 'a'
            start_pos = (x, y)
            lowest_elevations += [(x, y)]
        elif current_elevation == 'a':
            lowest_elevations += [(x, y)]
        elif current_elevation == 'E':
            current_elevation = 'z'
            end_pos = (x, y)
        # check left
        if x != 0:
            left_elevation = elmap[y][x - 1]
            left_pos = (x - 1, y)
            if left_elevation == 'S':
                left_elevation = 'a'
            if left_elevation == 'E':
                left_elevation = 'z'
            if ord(left_elevation) - ord(current_elevation) < 2:
                G.add_edge(current_pos, left_pos)
        # check right
        if x != (cols - 1):
            right_elevation = elmap[y][x + 1]
            right_pos = (x + 1, y)
            if right_elevation == 'S':
                right_elevation = 'a'
            if right_elevation == 'E':
                right_elevation = 'z'            
            if ord(right_elevation) - ord(current_elevation) < 2:
                G.add_edge(current_pos, right_pos)
        # check up
        if y != 0:
            up_elevation = elmap[y - 1][x]
            up_pos = (x, y - 1)
            if up_elevation == 'S':
                up_elevation = 'a'
            if up_elevation == 'E':
                up_elevation = 'z'            
            if ord(up_elevation) - ord(current_elevation) < 2:
                G.add_edge(current_pos, up_pos)
        # check down
        if y != (rows - 1):
            down_elevation = elmap[y + 1][x]
            down_pos = (x, y + 1)
            if down_elevation == 'S':
                down_elevation = 'a'
            if down_elevation == 'E':
                down_elevation = 'z'            
            if ord(down_elevation) - ord(current_elevation) < 2:
                G.add_edge(current_pos, down_pos)
# Calculate the shortest path between start and finish
shortest = nx.shortest_path(G, start_pos, end_pos)
print('Part 1: shortest path is ' + str(len(shortest) - 1))
# Now for part 2
shortest_path = 9999999999999999999999
for elevation in lowest_elevations:
    if nx.has_path(G, elevation, end_pos): # In my input there was at least 1 'a' elevation that could not reach E
        shortest = nx.shortest_path(G, elevation, end_pos)
        if (len(shortest) - 1) < shortest_path:
            shortest_path = (len(shortest) - 1)
print('Part 2: shortest path from any lowest elevation is ' + str(shortest_path))
      