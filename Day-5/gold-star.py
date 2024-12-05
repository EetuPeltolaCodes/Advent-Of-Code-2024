import numpy as np

def order_list(list, rules):
    firsts = []
    follows = []
    new_list = []
    for rule in rules:
        firsts.append(rule[0])
        follows.append(rule[1])
    
    for node in list:
        if node not in follows:
            first_in_order = node
            break
    
    new_list.append(first_in_order)
    current_node = first_in_order
    remaining_nodes = [node for node in list if node != current_node]
    while len(remaining_nodes) > 0:
        ways = {node: 0 for node in remaining_nodes}
        for first in firsts:
            if first in remaining_nodes:
                ways[first] += 1 
        current_node = max(ways, key=ways.get)
        new_list.append(current_node)
        remaining_nodes = [node for node in remaining_nodes if node != current_node]
                      
    middle = int(new_list[int((len(new_list) - 1)/2)])
    
    return middle

def check_list(list, rules):
    checked = []
    middle = 0
    call = False
    for node in list:
        for rule in rules:
            if node in rule[0]:
                if rule[1] in checked:
                    call = True
                    break
        if call:
            break
        checked.append(node)
    if call:
        return order_list(list, rules)
    
    return 0

with open('Day-5\input.txt') as f:
    data = f.read().splitlines()
    idx = np.where(np.array(data) == '')[0][0]
    rules = data[:idx]
    lists = data[idx+1:]
    
    middle_sum = 0
    for list in lists:
        list = list.split(',')
        list_rules = []
        for rule in rules:
            rule = rule.split('|')
            if rule[0] in list and rule[1] in list:
                list_rules.append(rule)
        
        middle_sum += check_list(list, list_rules)
        
    print(f'The sum of the middle values is {middle_sum}')