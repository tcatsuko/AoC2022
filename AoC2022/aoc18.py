f = open('aoc18.txt','rt')
cubes = []
max_x = 0
max_y = 0
max_z = 0
cube_locations = []
for line in f:
    text_location = line[:-1].split(',')
    location = [int(x) for x in text_location]
    cube_info = [location,6]
    cubes += [cube_info]
    cube_locations += [tuple(location)]
f.close()
def is_adjacent(current_cube, next_cube):
    cube_test = [abs(current_cube[0]-next_cube[0]), abs(current_cube[1] - next_cube[1]), abs(current_cube[2]-next_cube[2])]
    count_common = cube_test.count(0)
    count_adjacent = cube_test.count(1)
    if count_common == 2 and count_adjacent == 1:
        return True
    else:
        return False
for x in range(len(cubes)):
    remaining_length = x + 1
    current_cube = cubes[x]
    if current_cube[0][0] > max_x:
        max_x = current_cube[0][0]
    if current_cube[0][1] > max_y:
        max_y = current_cube[0][1]
    if current_cube[0][2] > max_z:
        max_z = current_cube[0][2]
    for y in range(remaining_length, len(cubes)):
        # find out distances
        next_cube = cubes[y]
        # cube_test = [abs(current_cube[0][0]-next_cube[0][0]), abs(current_cube[0][1] - next_cube[0][1]), abs(current_cube[0][2]-next_cube[0][2])]
        # count_common = cube_test.count(0)
        # count_adjacent = cube_test.count(1)
        adjacent = is_adjacent(current_cube[0], next_cube[0])
        # if count_common == 2 and count_adjacent == 1:
        if adjacent == True:
            cubes[x][1] -= 1
            cubes[y][1] -= 1
# Count surface area
surface_area = 0
surface_area_cubes = {}
for cube in cubes:
    surface_area += cube[1]
    if cube[1] > 0:
        surface_area_cubes[tuple(cube[0])] = cube[1]
print('Part 1: surface area is ' + str(surface_area))
exterior_nodes = set()
# Now flood fill
# test along y
exterior_faces = 0

flood_tested = []
flood_queue = []

flood_queue += [(-1,-1,-1)]
while len(flood_queue) > 0:
    point_to_test = flood_queue.pop(0)
    flood_tested += [point_to_test]
    x = point_to_test[0]
    y = point_to_test[1]
    z = point_to_test[2]
    up_cube = None
    down_cube = None
    left_cube = None
    right_cube = None
    forward_cube = None
    backward_cube = None

    if x != -1:
        left_cube = (x - 1, y, z)
    
    if x < max_x + 1:
        right_cube = (x+1,y,z)
    if y != -1:
        forward_cube = (x,y-1,z)
    if y < max_y + 1:
        backward_cube = (x,y+1,z)
    if z != -1:
        down_cube = (x, y, z - 1)
    if z < max_z + 1:
        up_cube = (x,y,z+1)
    # test cubes
    if left_cube is not None and left_cube not in flood_tested:
        if left_cube in cube_locations:
            exterior_faces += 1
            left_cube = None
        else:
            if left_cube not in flood_queue:
                flood_queue += [left_cube]
    if right_cube is not None and right_cube not in flood_tested:
        if right_cube in cube_locations:
            exterior_faces += 1
            right_cube = None
        else:
            if right_cube not in flood_queue:
                flood_queue += [right_cube]
    if up_cube is not None and up_cube not in flood_tested:
        if up_cube in cube_locations:
            exterior_faces += 1
            up_cube = None
        else:
            if up_cube not in flood_queue:
                flood_queue += [up_cube]
    if down_cube is not None and down_cube not in flood_tested:
        if down_cube in cube_locations:
            exterior_faces += 1
            down_cube = None
        else:
            if down_cube not in flood_queue:
                flood_queue += [down_cube]
    if forward_cube is not None and forward_cube not in flood_tested:
        if forward_cube in cube_locations:
            exterior_faces += 1
            forward_cube = None
        else:
            if forward_cube not in flood_queue:
                flood_queue += [forward_cube]
    if backward_cube is not None and backward_cube not in flood_tested:
        if backward_cube in cube_locations:
            exterior_faces += 1
            backward_cube = None
        else:
            if backward_cube not in flood_queue:
                flood_queue += [backward_cube]
print('Part 2: exterior surface area is ' + str(exterior_faces))
