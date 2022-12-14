from parse import *
import numpy as np
import cvxpy as cp

blueprints = []
f = open('aoc19.txt','rt')
for line in f:
    line = line[:-1]
    result = parse('Blueprint {bp}: Each ore robot costs {oreorecost} ore. Each clay robot costs {clayorecost} ore. Each obsidian robot costs {obsorecost} ore and {obsclaycost} clay. Each geode robot costs {geoorecost} ore and {geoobscost} obsidian.', line)
    blueprint = {}
    blueprint['ore'] = {'ore':int(result['oreorecost'])}
    blueprint['clay'] = {'ore':int(result['clayorecost'])}
    blueprint['obsidian'] = {'ore':int(result['obsorecost']), 'clay':int(result['obsclaycost'])}
    blueprint['geode'] = {'ore':int(result['geoorecost']), 'obsidian':int(result['geoobscost'])}

    blueprints += [blueprint]
def max_geode(blueprint, minutes):
    materials_cost = np.array([[blueprint['ore']['ore'], blueprint['clay']['ore'], blueprint['obsidian']['ore'], blueprint['geode']['ore']],[0, 0, blueprint['obsidian']['clay'],0],[0,0,0,blueprint['geode']['obsidian']],[0,0,0,0]])
    
    material_vars = []
    robot_vars = []
    produced_vars = []
    constraints = []
    for minute in range(minutes + 1):   # problem description means we need to add a minute
        materials = cp.Variable(4)
        robots = cp.Variable(4)
        decisions = cp.Variable(4, boolean = True)
        if minute == 0:
            # first minute, set things up
            constraints.append(materials == 0)  # Start with no materials
            constraints.append(robots[0] == 1)  # Start with one ore robot
            constraints.append(robots[1:] == 0) # We dont have any other robots
            constraints.append(decisions== 0) # We haven't decided to do anything yet
        else:
            last_materials = material_vars[-1]
            constraints.append(robots == robot_vars[-1] + produced_vars[-1]) 
            constraints.append(cp.sum(decisions) <= 1)  # Can only propduce one robot
            constraints.append(materials_cost @ decisions<= last_materials) # What can we build?
            constraints.append(materials == (last_materials + robots - (materials_cost @ decisions)))
        robot_vars.append(robots)
        material_vars.append(materials)
        produced_vars.append(decisions)
    solver_objective = cp.Maximize(material_vars[-1][3]) #Maximize geodes
    problem = cp.Problem(solver_objective, constraints)
    problem.solve()
    return problem.value

blueprint_geodes = []
for idx, blueprint in enumerate(blueprints):
    max_geodes = max_geode(blueprint, 24)
    blueprint_geodes += [int(max_geodes)]

# find the quality levels
quality_levels = []
for x in range(len(blueprint_geodes)):
    quality_levels += [(x + 1) * blueprint_geodes[x]]
print('Part 1: sum of all quality levels is ' + str(sum(quality_levels)))

# Part 2
new_blueprints = blueprints[:3]

blueprint_geodes = []
for blueprint in new_blueprints:
    max_geodes = max_geode(blueprint, 32)
    blueprint_geodes += [int(max_geodes)]

answer = 1
for x in blueprint_geodes:
    answer *= x
print(blueprint_geodes)
print('Part 2: multiplying the max geodes of the first three geodes yields ' + str(answer))

