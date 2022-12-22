from sympy import symbols, Eq, solve
f = open('aoc21.txt','rt')
monkeys = {}
human_oper1_count = 0
human_oper2_count = 0

for line in f:
    stripped_line = line[:-1]
    [monkey, result] = stripped_line.split(': ')
    split_result = result.split(' ')
    monkeys[monkey] = {}
    if len(split_result) == 3:
        # It's an expression
        monkeys[monkey]['value'] = None
        monkeys[monkey]['oper1'] = split_result[0]
        if split_result[0] == 'humn':
            human_oper1_count += 1
        monkeys[monkey]['operator'] = split_result[1]
        monkeys[monkey]['oper2'] = split_result[2]
        if split_result[2] == 'humn':
            human_oper2_count += 1
    else:
        monkeys[monkey]['value'] = split_result[0]
f.close()

def get_value(monkeys, monkey_name):
    if monkeys[monkey_name]['value'] != None:
        return monkeys[monkey_name]['value']
    else:
        oper1 = get_value(monkeys, monkeys[monkey_name]['oper1'])
        oper2 = get_value(monkeys, monkeys[monkey_name]['oper2'])
        final_value = str(eval(oper1 + monkeys[monkey_name]['operator'] + oper2))
        monkeys[monkey_name]['value'] = final_value
        return final_value

root_value = get_value(monkeys, 'root')
print('Part 1: root\'s value is ' + root_value)
# Now do it all over again
f = open('aoc21.txt','rt')
monkeys = {}
human_oper1_count = 0
human_oper2_count = 0

number_monkeys = {}
equation_monkeys = {}

for line in f:
    stripped_line = line[:-1]
    [monkey, result] = stripped_line.split(': ')
    if monkey == 'humn':
        humn = symbols('humn')
        number_monkeys['humn'] = humn
        continue
    elif monkey == 'root':
        split_equation = result.split(' + ')
        left_side = split_equation[0]
        right_side = split_equation[1]
        continue
    split_result = result.split(' ')
    if len(split_result) == 1:
        number_monkeys[monkey] = int(result)
    else:
        equation_monkeys[monkey] = result
   
while len(equation_monkeys) > 0:
    equations_to_delete = set()
    for monkey in equation_monkeys:
        split_equation = equation_monkeys[monkey].split(' ')
        oper1 = split_equation[0]
        oper2 = split_equation[2]
        if (oper1 in number_monkeys) and (oper2 in number_monkeys):
            oper1 = number_monkeys[split_equation[0]]
            oper2 = number_monkeys[split_equation[2]]
            if split_equation[1] == '+':
                number_monkeys[monkey] = oper1 + oper2
            elif split_equation[1] == '-':
                number_monkeys[monkey] = oper1 - oper2
            elif split_equation[1] == '*':
                number_monkeys[monkey] = oper1 * oper2
            elif split_equation[1] == '/':
                number_monkeys[monkey] = oper1 / oper2
            equations_to_delete.add(monkey)
    for monkey in equations_to_delete:
        del(equation_monkeys[monkey])

left_eq = number_monkeys[left_side]
right_eq = number_monkeys[right_side]

solution = solve(Eq(left_eq, right_eq), humn)

print('Part 2: humn is ' + str(solution[0]))




