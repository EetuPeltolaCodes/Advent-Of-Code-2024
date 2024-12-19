def check_message(rules, message):
    if message == '':
        return True
    for rule in rules:
        if message.startswith(rule):
            if check_message(rules, message[len(rule):]):
                return True
    return False

with open('Day-19/input.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.replace(" ","").split(',')
    messages = messages.split('\n')

possible_designs = 0
for message in messages:
    for rule in rules:
        if message.startswith(rule):
            if check_message(rules, message[len(rule):]):
                possible_designs += 1
                break

print(f'There are {possible_designs} possible designs of the towels.')            