import networkx as nx
import math
import itertools

f = open('aoc16.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# Start to parse the data
nodes = {}
G = nx.Graph()
for line in raw_input:
    [node_info, destinations] = line.split('; ')
    node_name = node_info.split(' ')[1]
    node_flow = int(node_info.split('=')[1])
    text_destinations = destinations.split(' valve')[1].split(' ')[1:]
    node_destinations = []
    for item in text_destinations:
        node_destinations += [item.split(',')[0]]
    nodes[node_name] = {}
    nodes[node_name]['flow'] = node_flow
    nodes[node_name]['destinations'] = node_destinations
for node in nodes:
    node_info = nodes[node]
    for destination in node_info['destinations']:
        G.add_edge(node, destination)
# Find all valves that actually increase flow
flow_valves = []
for node in nodes:
    if nodes[node]['flow'] != 0 and node != 'AA':
        flow_valves += [node]
# Now iterate between AA and all of those paths
floyd = nx.floyd_warshall(G)
print()
global_best = 0


def best_path(current_valve, unvisited_valves, floyd, time, nodes, start_pressure, time_allowed, total_flow):
    global global_best
    
    new_flow = total_flow + nodes[current_valve]['flow']
    if nodes[current_valve]['flow'] != 0:  
        time += 1
    start_pressure += new_flow
    best_pressure = start_pressure 
    best_time = time
    best_flow = new_flow
    remaining_time = time_allowed - time
    best_pressure = (remaining_time * best_flow) + start_pressure
    start_best_pressure = best_pressure

        
    for valve in unvisited_valves:
        
        time_needed =  int(floyd[current_valve][valve])
        if (time + time_needed) > time_allowed:
            continue
        new_unvisited = unvisited_valves[:]
        new_unvisited.remove(valve)
        new_pressure = start_pressure + (time_needed* new_flow)
        [result_pressure, new_time, remaining_flow, remaining_time] = best_path(valve, new_unvisited, floyd, time_needed+time, nodes, new_pressure, time_allowed, new_flow)

            
        if result_pressure > best_pressure:
            best_pressure = result_pressure
            best_time = remaining_flow
            best_flow = new_flow

    return [best_pressure, best_time, best_flow, time_allowed - (time - best_time)]
flow_valves.sort()
half_nodes = len(flow_valves) // 2 + 1
part1_result = best_path('AA', flow_valves, floyd, 1, nodes, 0, 30, 0)
print('Part 1: best flow possible is ' + str(part1_result[0]))
global_best = 0
seven_nodes = list(itertools.combinations(flow_valves, 7))
six_nodes = list(itertools.combinations(flow_valves, 6))
# Iterate over the six node list
seven_memos = {}

for six_list in six_nodes:
    human = list(six_list)
    human_best = best_path('AA', human, floyd, 1, nodes, 0, 26, 0)[0]
    for seven_tuple in seven_nodes:
        elephant = list(seven_tuple)
        test = True
        
        for item in elephant:
            if item in human:
                test = False
                break
        if test == True:
            if seven_tuple not in seven_memos:
                elephant_best = best_path('AA', elephant, floyd, 1, nodes, 0, 26, 0)[0]
                seven_memos[seven_tuple] = elephant_best
            else:
                elephant_best = seven_memos[seven_tuple]
            best_score = human_best + elephant_best
            if best_score > global_best:
                global_best = best_score


print('Part 2: best flow possible is ' + str(global_best))

