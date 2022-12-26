f = open ('aoc22.txt','rt')
raw_input = []
found_instructions = False
for line in f:
    if line == '\n' and found_instructions == False:
        board_map = raw_input[:]
        raw_input = []
        found_instructions = True
        continue
    raw_input += [line[:-1]]

f.close()
# Normalize the length of each row.  Somehwat hardcoded to my input
max_length = len(board_map[0])
for idx, row in enumerate(board_map):
    row_length = len(row)
    if row_length < max_length:
        row += ' ' * (max_length - row_length)
        board_map[idx] = row
    
def move(board_map, edge_indices, position, facing, distance_str):
    steps = int(distance_str)
    max_down = len(board_map)
    max_col = len(board_map[0])
    for step in range(steps):
        if facing == 0:
            # move right
            row = position[1]
            next_x = position[0] + 1
            
            if next_x == len(board_map[0]):
                next_x = 0
            check_spot = board_map[row][next_x]
            while check_spot == ' ':
                next_x += 1
                if next_x == len(board_map[0]):
                    next_x = 0
                check_spot = board_map[row][next_x]
            if check_spot == '.':
                position = [next_x, row]
        elif facing == 1:
            column = position[0]
            next_y = position[1] + 1
            if next_y == max_down:
                next_y = 0
            check_spot = board_map[next_y][column]
            while check_spot == ' ':
                next_y += 1
                if next_y == len(board_map):
                    next_y = 0
                check_spot = board_map[next_y][column]
            if check_spot == '.':
                position = [column, next_y]
        elif facing == 2:
            row = position[1]
            next_x = position[0] - 1
            if next_x < edge_indices[row][0]:
                next_x = edge_indices[row][1]
            check_spot = board_map[row][next_x]
            while check_spot == ' ':
                next_x -= 1
                if next_x == -1:
                    next_x = len(board_map[0]) - 1
                    check_spot = board_map[row][next_x]
            if check_spot == '.':
                position = [next_x, row]
        elif facing == 3:
            # move up
            column = position[0]
            next_y = position[1] - 1
            if next_y == -1:
                next_y = len(board_map) - 1
            max_current_row_length = len(board_map[next_y])
            check_spot = board_map[next_y][column]
            while check_spot == ' ':
                next_y -= 1
                if next_y == -1:
                    next_y = len(board_map) - 1
                check_spot = board_map[next_y][column]
            if check_spot == '.':
                position = [column, next_y]
    return [position, facing]


facing = 0
# Find initial location
start_pos = [board_map[0].find('.'), 0]
instructions = [x for x in raw_input[0]]
# Do some housekeeping to determine the wraparound points L-R
edge_indices = []
for x in range(len(board_map)):
    current_row = board_map[x]
    left_open = current_row.find('.') if '.' in current_row else 10000000000000000
    left_wall = current_row.find('#') if '#' in current_row else 10000000000000000
    left_start = left_open if left_open < left_wall else left_wall
    right_open = current_row.rfind('.') if '.' in current_row else -1
    right_wall = current_row.rfind('#') if '#' in current_row else -1
    right_start = right_open if right_open > right_wall else right_wall
    edge_indices += [[left_start, right_start]]
# Now game loop
distance_str = ''
position = start_pos[:]

while instructions:
    if instructions[0].isdigit() == False:
        # Move
        position, facing = move(board_map, edge_indices, position, facing, distance_str)
        # It's a direction change
        turn = instructions.pop(0)
        if turn == 'R':
            facing += 1
            if facing == 4:
                facing = 0
        else:
            facing -= 1
            if facing == -1:
                facing = 3
        distance_str = ''
        continue
    distance_str += instructions.pop(0)
position, facing = move(board_map, edge_indices, position, facing, distance_str)
score = (1000 * (position[1] + 1)) + (4 * (position[0] + 1)) + facing
print('Part 1: score is ' + str(score))
position = start_pos[:]
# Part 2
# Build rotations
# Hardcoded
position = [0,0]
def move_p2(board_map, position, facing, face, distance_str):
   
   
    x = position[0]
    y = position[1]
    # Determine face
    face_number = face
    # Build individual faces
    faces = []
    faces += [[]]
    # face 1
    current_face = []
    if distance_str == '27':
        print()
    for y in range(50):
        current_face += [board_map[y][50:100]]
    faces += [current_face]
    # face 2
    current_face = []
    for y in range(50):
        current_face += [board_map[y][100:]]
    faces += [current_face]
    # face 3
    current_face = []
    for y in range(50,100):
        current_face += [board_map[y][50:100]]
    faces += [current_face]
    current_face = []
    # face 4
    for y in range(100,150):
        current_face += [board_map[y][:50]]
    faces += [current_face]
    # face 5
    current_face = []
    for y in range(100,150):
        current_face += [board_map[y][50:100]]
    faces += [current_face]
    current_face = []

    for y in range(150,200):
        current_face += [board_map[y][:50]]
    faces += [current_face]

    steps = int(distance_str)
    max_down = len(board_map)
    max_col = len(board_map[0])
    

    for step in range(steps):
        if position[0] < 0 or position[0] > 50 or position[1] < 0 or position[1] > 50:
            print()
        current_face = faces[face]
        next_face_number = face
        next_facing = facing
        next_face = current_face
        if facing == 0:
            # move right
            row = position[1]
            next_x = position[0] + 1
            next_position = [position[0] + 1, row]
            if next_x == len(current_face[0]):
                # Move faces
                if face == 1:
                    next_face = faces[2]
                    next_face_number = 2
                    next_facing = 0
                    next_position = [0, position[1]]
                elif face == 2:
                    next_face = faces[5]
                    next_face_number = 5
                    next_facing = 2
                    next_position = [len(next_face[0]) - 1, len(next_face) - 1 - position[1]]
                elif face == 3:
                    next_face = faces[2]
                    next_face_number = 2
                    next_facing = 3
                    next_position = [position[1], len(next_face) - 1]
                elif face == 4:
                    next_face = faces[5]
                    next_face_number = 5
                    next_facing = 0
                    next_position = [0, position[1]]
                elif face == 5:
                    next_face = faces[2]
                    next_face_number = 2
                    next_facing = 2
                    next_position = len(next_face[0]) - 1, len(next_face) - 1 - position[1]
                elif face == 6:
                    next_face = faces[5]
                    next_face_number = 5
                    next_facing = 3
                    next_position = [position[1], len(next_face) - 1]
        elif facing == 1:
            column = position[0]
            next_y = position[1] + 1
            next_position = [column, next_y]
            if next_y == len(current_face):
                if face == 1:
                    next_face = faces[3]
                    next_face_number = 3
                    next_facing = 1
                    next_position = [position[0], 0]
                elif face == 2:
                    next_face = faces[3]
                    next_face_number = 3
                    next_facing = 2
                    next_position = [len(next_face[0]) - 1, position[0]]
                elif face == 3:
                    next_face = faces[5]
                    next_face_number = 5
                    next_facing = 1
                    next_position = [position[0], 0]
                elif face == 4:
                    next_face = faces[6]
                    next_face_number = 6
                    next_facing = 1
                    next_position = [position[0], 0]
                elif face == 5:
                    next_face = faces[6]
                    next_face_number = 6
                    next_facing = 2
                    next_position = [len(next_face[0]) - 1, position[0]]
                elif face == 6:
                     next_face = faces[2]
                     next_face_number = 2
                     next_facing = 1
                     next_position = [position[0], 0]
        elif facing == 2:
            row = position[1]
            next_x = position[0] - 1
            next_position = [next_x, row]
            if next_x < 0:
                if face == 1:
                    next_face = faces[4]
                    next_face_number =4
                    next_facing = 0
                    next_position = [0, len(next_face) - 1 - position[1]]
                elif face == 2:
                    next_face = faces[1]
                    next_face_number = 1
                    next_facing = 2
                    next_position = [len(next_face[0]) - 1, position[1]]
                elif face == 3:
                    next_face = faces[4]
                    next_face_number = 4
                    next_facing = 1
                    next_position = [position[1], 0]
                elif face == 4:
                    next_face = faces[1]
                    next_face_number = 1
                    next_facing = 0
                    next_position = [0, len(next_face) - 1 - position[1]]
                elif face == 5:
                    next_face = faces[4]
                    next_face_number = 4
                    next_facing = 2
                    next_position =[len(next_face[0]) - 1, position[1]]
                elif face == 6:
                    next_face = faces[1]
                    next_face_number = 1
                    next_facing = 1
                    next_position = [position[1], 0]
        elif facing == 3:
            # move up
            column = position[0]
            next_y = position[1] - 1
            next_position = [column, next_y]
            if next_y == -1:
                if face == 1:
                    next_face = faces[6]
                    next_face_number = 6
                    next_facing = 0
                    next_position = [0, position[0]]
                elif face == 2:
                    next_face = faces[6]
                    next_face_number = 6
                    next_facing = 3
                    next_position = [position[0], len(next_face) - 1]
                elif face == 3:
                    next_face = faces[1]
                    next_face_number = 1
                    next_facing = 3
                    next_position = [position[0], len(next_face) - 1]
                elif face == 4:
                    next_face = faces[3]
                    next_face_number = 3
                    next_facing = 0
                    next_position = [0, position[0]]
                elif face == 5:
                    next_face = faces[3]
                    next_face_number = 3
                    next_facing = 3
                    next_position = [position[0], len(next_face) - 1]
                elif face == 6:
                    next_face = faces[4]
                    next_face_number = 4
                    next_facing = 3
                    next_position = [position[0], len(next_face) - 1]

            

        if 50 in next_position :
            print()
        check_spot = next_face[next_position[1]][next_position[0]]
        if check_spot == '.':
            if position[1] == 49:
                print()
            position = next_position
            facing = next_facing
            face = next_face_number
            current_face = next_face

    

    return [position, facing, face]
instructions = [x for x in raw_input[0]]
distance_str = ''
position = start_pos[:]
position = [0,0]
face = 1
while instructions:
    if instructions[0].isdigit() == False:
        # Move
        position, facing, face = move_p2(board_map, position, facing, face, distance_str)
        # It's a direction change
        turn = instructions.pop(0)
        if turn == 'R':
            facing += 1
            if facing == 4:
                facing = 0
        else:
            facing -= 1
            if facing == -1:
                facing = 3
        distance_str = ''
        continue
    distance_str += instructions.pop(0)
position, facing, face = move_p2(board_map, position, facing, face, distance_str)
width = 50

offsets = []
offsets += [[]]
offsets += [[1,0]]
offsets += [[2,0]]
offsets += [[1,1]]
offsets += [[0,2]]
offsets += [[1,2]]
offsets += [[0,3]]
offset_x = width * (offsets[face][0])
offset_y = width * (offsets[face][1])

offset_position = [position[0] + offset_x, position[1] + offset_y]

score = (1000 * (offset_position[1] + 1)) + (4 * (offset_position[0] + 1)) + facing
print('Part 1: score is ' + str(score))
# 162601 too high
#162201 too high