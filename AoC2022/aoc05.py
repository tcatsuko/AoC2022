import re
demo = False

# Will need to hand code the input for most of it, parsing looks difficult
stacks = {}
# demo
if demo == True:
    f = open('test_aoc05.txt','rt')
    raw_input = []
    for line in f:
        raw_input += [line[:-1]]
    f.close()    
    stacks['1'] = ['Z','N']
    stacks['2'] = ['M','C','D']
    stacks['3'] = ['P']
else:
    f = open('aoc05.txt','rt')
    raw_input = []
    for line in f:
        raw_input += [line[:-1]]
    f.close()    
    stacks['1'] = ['C','Z','N','B','M','W','Q','V']
    stacks['2'] = ['H','Z','R','W','C','B']
    stacks['3'] = ['F','Q','R','J']
    stacks['4'] = ['Z','S','W','H','F','N','M','T']
    stacks['5'] = ['G','F','W','L','N','Q','P']
    stacks['6'] = ['L','P','W']
    stacks['7'] = ['V','B','D','R','G','C','Q','J']
    stacks['8'] = ['Z','Q','N','B','W']
    stacks['9'] = ['H','L','F','C','G','T','J']
for line in raw_input:
    moves = re.findall(r'\d+',line)
    from_stack= stacks[moves[1]]
    to_stack = stacks[moves[2]]
    number = int(moves[0])
    for item in range(number):
        to_stack += from_stack.pop(-1)
top_crates = ''
for x in range(len(stacks)):
    index = str(x + 1)
    top_crates += stacks[index][-1]
print('Part 1: the top crates are ' + top_crates)
# Part 2
if demo == True:
    f = open('test_aoc05.txt','rt')
    raw_input = []
    for line in f:
        raw_input += [line[:-1]]
    f.close()    
    stacks['1'] = ['Z','N']
    stacks['2'] = ['M','C','D']
    stacks['3'] = ['P']
else:
    f = open('aoc05.txt','rt')
    raw_input = []
    for line in f:
        raw_input += [line[:-1]]
    f.close()    
    stacks['1'] = ['C','Z','N','B','M','W','Q','V']
    stacks['2'] = ['H','Z','R','W','C','B']
    stacks['3'] = ['F','Q','R','J']
    stacks['4'] = ['Z','S','W','H','F','N','M','T']
    stacks['5'] = ['G','F','W','L','N','Q','P']
    stacks['6'] = ['L','P','W']
    stacks['7'] = ['V','B','D','R','G','C','Q','J']
    stacks['8'] = ['Z','Q','N','B','W']
    stacks['9'] = ['H','L','F','C','G','T','J']
for line in raw_input:
    moves = re.findall(r'\d+',line)
    from_stack= stacks[moves[1]]
    to_stack = stacks[moves[2]]
    number = int(moves[0])
    temp_stack = []
    for item in range(number):
        temp_stack += from_stack.pop(-1)
    temp_stack.reverse()
    to_stack += temp_stack
top_crates = ''
for x in range(len(stacks)):
    index = str(x + 1)
    top_crates += stacks[index][-1]
print('Part 2: the top crates are ' + top_crates)
