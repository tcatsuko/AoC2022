f = open('aoc02.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Create games
games = []
for line in raw_input:
    games += [line.split(' ')]
print()
score = 0
# Now calculate the score
for game in games:
    opponent = game[0]
    you = game[1]
    if you == 'X':
        score += 1
    elif you == 'Y':
        score += 2
    elif you == 'Z':
        score += 3
    if opponent == 'A': #Opponent plays rock
        if you == 'X':
            score += 3
        elif you == 'Y':
            score += 6
    elif opponent == 'B':
        if you == 'Y':
            score += 3
        elif you == 'Z':
            score += 6
    elif opponent == 'C':
        if you == 'Z':
            score += 3
        elif you == 'X':
            score += 6
print('Part 1: total score is ' + str(score))
# Now for part 2
score = 0
for game in games:
    opponent = game[0]
    you = game[1]
    if you == 'X':
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 1
        elif opponent == 'C':
            score += 2
    elif you == 'Y':
        score += 3
        if opponent == 'A':
            score += 1
        elif opponent == 'B':
            score += 2
        elif opponent == 'C':
            score += 3
    elif you == 'Z':
        score += 6
        if opponent == 'A':
            score += 2
        elif opponent == 'B':
            score += 3
        elif opponent == 'C':
            score += 1
print('Part 2: Score is ' + str(score))
