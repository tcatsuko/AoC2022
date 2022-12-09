f = open('aoc09.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
visited_spots = set()

num_knots = 2
rope = []
for x in range(num_knots):
    rope += [(0,0)]
for line in raw_input:
    [direction, distance] = line.split(' ')
    distance = int(distance)
    for steps in range(distance):
        if direction == 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])
        elif direction == 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif direction == 'U':
            rope[0] = (rope[0][0], rope[0][1] + 1)
        elif direction == 'D':
            rope[0] = (rope[0][0], rope[0][1] - 1)
            # Now simulate the rope movement
        for idx, knot in enumerate(rope):
            # do not treat the tail as head of a sub-rope
            if idx == len(rope) - 1:
                continue
            head_x = knot[0]
            head_y = knot[1]
            tail_x = rope[idx + 1][0]
            tail_y = rope[idx + 1][1]
            # check to see if movement needed
            if (abs(head_x - tail_x) < 2) and (abs(head_y - tail_y) < 2):
                # close enough, continue
                continue
            else:
                # need to move tail
                if head_x - tail_x != 0:
                    tail_x = tail_x + 1 if (head_x > tail_x) else tail_x - 1
                if head_y - tail_y != 0:
                    tail_y = tail_y + 1 if (head_y > tail_y) else tail_y - 1
            rope[idx + 1] = (tail_x, tail_y)
        visited_spots.add(rope[-1])
print('Part 1: the tail of a ' + str(num_knots) + ' knot rope visited ' + str(len(visited_spots)) + ' spots')

visited_spots.clear()
num_knots = 10
rope = []
for x in range(num_knots):
    rope += [(0,0)]
for line in raw_input:
    [direction, distance] = line.split(' ')
    distance = int(distance)
    for steps in range(distance):
        if direction == 'R':
            rope[0] = (rope[0][0] + 1, rope[0][1])
        elif direction == 'L':
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif direction == 'U':
            rope[0] = (rope[0][0], rope[0][1] + 1)
        elif direction == 'D':
            rope[0] = (rope[0][0], rope[0][1] - 1)
            # Now simulate the rope movement
        for idx, knot in enumerate(rope):
            # do not treat the tail as head of a sub-rope
            if idx == len(rope) - 1:
                continue
            head_x = knot[0]
            head_y = knot[1]
            tail_x = rope[idx + 1][0]
            tail_y = rope[idx + 1][1]
            # check to see if movement needed
            if (abs(head_x - tail_x) < 2) and (abs(head_y - tail_y) < 2):
                # close enough, continue
                continue
            else:
                # need to move tail
                if head_x - tail_x != 0:
                    tail_x = tail_x + 1 if (head_x > tail_x) else tail_x - 1
                if head_y - tail_y != 0:
                    tail_y = tail_y + 1 if (head_y > tail_y) else tail_y - 1
            rope[idx + 1] = (tail_x, tail_y)
        visited_spots.add(rope[-1])
print('Part 2: the tail of a ' + str(num_knots) + ' knot rope visited ' + str(len(visited_spots)) + ' spots')


