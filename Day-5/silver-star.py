import numpy as np


def check_list(list, rules):
    checked = []
    middle = 0
    for node in list:
        for rule in rules:
            if node in rule[0]:
                if rule[1] in checked:
                    return 0
        checked.append(node)

    middle = int(list[int((len(list) - 1)/2)])
    
    return middle

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