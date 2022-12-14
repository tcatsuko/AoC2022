f = open('aoc14.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Step 1: find the bounds of the rocks and build instructions
min_x = 1000000000000000000000000000000000000
max_x = -1
min_y = 1000000000000000000000000000000000000
max_y = -1
lines = []

for line in raw_input:
    split_points = line.split(' -> ')
    current_line = []
    for point in split_points:
        [x,y] = point.split(',')
        x = int(x)
        y = int(y)
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        current_line += [(x,y)]
    lines += [current_line]
# Build empty cavern
cavern = []
for y in range(max_y + 1):
    current_row = []
    for x in range(max_x + 1):
        current_row += '.'
    cavern += [current_row]
# Put the rocks in
for line in lines:
    for counter in range(len(line) - 1):
        start_point = line[counter]
        end_point = line[counter + 1]
        if start_point[1] == end_point[1]:
            # Horizontal line
            row = start_point[1]
            start_x = start_point[0] if start_point[0] < end_point[0] else end_point[0]
            end_x = end_point[0] + 1 if end_point[0] > start_point[0] else start_point[0] + 1
            for x in range(start_x, end_x):
                cavern[row][x] = '#'
        else:
            column = start_point[0]
            start_y = start_point[1] if start_point[1] < end_point[1] else end_point[1]
            end_y = end_point[1] + 1 if end_point[1] > start_point[1] else start_point[1] + 1
            for y in range(start_y, end_y):
                cavern[y][column] = '#'
sand_grains = 0
# Now start the main loop
infinite = False
while infinite == False:
    can_move = True
    pos = (500,0)
    while can_move == True:
        # Check down

        while True:
            # check down one
            if cavern[pos[1] + 1][pos[0]] == '.':
                pos = (pos[0], pos[1] + 1)
                if pos[1] >= max_y:
                    infinite = True
                    break
            else:
                break
        # Can't move down any more, check down left
        if infinite == True:
            break
        if cavern[pos[1] + 1][pos[0] - 1] == '.':
            pos = (pos[0] - 1, pos[1] + 1)
            if pos[1] == max_y:
                infinite = True
                break
            continue
        # Can't move down left, try down right
        if cavern[pos[1] + 1][pos[0] + 1] == '.':
            pos = (pos[0] + 1, pos[1] + 1)
            if pos[1] == max_y: 
                infinite = True
                break
            continue
        # Can't move down right either
        cavern[pos[1]][pos[0]] = 'o'
        sand_grains += 1
        can_move = False
print('Part 1: there are ' + str(sand_grains) + ' sand grains at rest.')

# Part 2 - doing it the hard way.  Just add 10000 to min and max x since it's not really infinite.

# Build empty cavern
cavern = []
for y in range(max_y + 1):
    current_row = []
    for x in range(max_x + 20001):
        current_row += '.'
    cavern += [current_row]
# Put the rocks in
for line in lines:
    for counter in range(len(line) - 1):
        start_point = line[counter]
        end_point = line[counter + 1]
        if start_point[1] == end_point[1]:
            # Horizontal line
            row = start_point[1]
            start_x = start_point[0] if start_point[0] < end_point[0] else end_point[0]
            end_x = end_point[0] + 1 if end_point[0] > start_point[0] else start_point[0] + 1
            start_x += 10000
            end_x += 10000
            for x in range(start_x, end_x):
                cavern[row][x] = '#'
        else:
            column = start_point[0]
            start_y = start_point[1] if start_point[1] < end_point[1] else end_point[1]
            end_y = end_point[1] + 1 if end_point[1] > start_point[1] else start_point[1] + 1
            for y in range(start_y, end_y):
                cavern[y][column + 10000] = '#'
# Build two more rows
current_row = ['.'] * (20000 + max_x)
cavern += [current_row]
current_row = ['#'] * (20000 + max_x)
cavern += [current_row]
max_y += 2
sand_grains = 0
# Now start the main loop
infinite = False
while infinite == False:
    can_move = True
    pos = (10500,0)
    while can_move == True:
        if cavern[0][10500] != '.':
            infinite = True
            break
        # Check down
        while True:
            # check down one
            if cavern[pos[1] + 1][pos[0]] == '.':
                pos = (pos[0], pos[1] + 1)
                if pos[1] >= max_y:
                    infinite = True
                    break
            else:
                break
        # Can't move down any more, check down left
        if infinite == True:
            break
        if cavern[pos[1] + 1][pos[0] - 1] == '.':
            pos = (pos[0] - 1, pos[1] + 1)
            if pos[1] == max_y:
                infinite = True
                break
            continue
        # Can't move down left, try down right
        if cavern[pos[1] + 1][pos[0] + 1] == '.':
            pos = (pos[0] + 1, pos[1] + 1)
            if pos[1] == max_y: 
                infinite = True
                break
            continue
        # Can't move down right either
        cavern[pos[1]][pos[0]] = 'o'
        sand_grains += 1
        can_move = False

print('Part 1: there are ' + str(sand_grains) + ' sand grains at rest.')