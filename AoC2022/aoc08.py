f = open('aoc08.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
tree_grid = []
for line in raw_input:
    new_row = []
    for tree in line:
        new_row += [int(tree)]
    tree_grid += [new_row]
print()
visible_trees = set()
rows = len(tree_grid)
columns = len(tree_grid[0])

# iterate each row from the left
for y in range(rows):
    current_height = -1
    for x in range(columns):
        if tree_grid[y][x] > current_height:
            visible_trees.add((x,y,tree_grid[y][x]))
            current_height = tree_grid[y][x]
# iterate each row from the right
for y in range(rows):
    current_height = -1
    for x in range(rows - 1, -1, -1):
        if tree_grid[y][x] > current_height:
            visible_trees.add((x,y,tree_grid[y][x]))
            current_height = tree_grid[y][x]

# iterate each column from the top
for x in range(columns):
    current_height = -1
    for y in range(rows):
        if tree_grid[y][x] > current_height:
            visible_trees.add((x,y,tree_grid[y][x]))
            current_height = tree_grid[y][x]
# Iterate each column from the bottom
for x in range(columns):
    current_height = -1
    for y in range(rows - 1, -1, -1):
        if tree_grid[y][x] > current_height:
            visible_trees.add((x,y,tree_grid[y][x]))
            current_height = tree_grid[y][x]
print('Part 1: there are ' + str(len(visible_trees)) + ' trees visible')

# Now to iterate for each tree.  Fun.
high_score = 0

for y in range(rows):
    for x in range(columns):
        current_tree_height = tree_grid[y][x]
        left_score = 0
        right_score = 0
        up_score = 0
        down_score = 0
        # check left:
        for search_x in range(x, -1, -1):
            if search_x == x:
                continue
            if tree_grid[y][search_x] < current_tree_height:
                left_score += 1
            elif tree_grid[y][search_x] >= current_tree_height:
                left_score += 1
                break
            
        # check right:
        for search_x in range(x, columns):
            if search_x == x:
                continue
            if tree_grid[y][search_x] < current_tree_height:
                right_score += 1
            elif tree_grid[y][search_x] >= current_tree_height:
                right_score += 1
                break
        
        # check up
        for search_y in range(y, -1, -1):
            if search_y == y:
                continue
            if tree_grid[search_y][x] < current_tree_height:
                up_score += 1
            elif tree_grid[search_y][x] >= current_tree_height:
                up_score += 1
                break
        # check down
        for search_y in range(y, rows):
            if search_y == y:
                continue
            if tree_grid[search_y][x] < current_tree_height:
                down_score += 1
            elif tree_grid[search_y][x] >= current_tree_height:
                down_score += 1
                break
        score = up_score * down_score * left_score * right_score
        if score > high_score:
            high_score = score
print('Part 2: Highest scenic score possible is ' + str(high_score))