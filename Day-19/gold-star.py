def check_message(rules, message, memo):
    if message in memo:
        return memo[message]
    if message == '':
        return 1
    count = 0
    for rule in rules:
        if message.startswith(rule):
            count += check_message(rules, message[len(rule):], memo)
    memo[message] = count
    return count

with open('Day-19/input.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.replace(" ","").split(',')
    messages = messages.split('\n')

possible_designs = 0
memo = {}
for message in messages:
    for rule in rules:
        if message.startswith(rule):
            possible_designs += check_message(rules, message[len(rule):], memo)

print(f'There are {possible_designs} possible designs of the towels.')