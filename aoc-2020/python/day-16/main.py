rules = {}
other_tickets = []
with open('input.txt') as file:
    line = next(file).strip()
    while line:
        field, field_rules = line.split(': ')
        rules[field] = [[int(i) for i in r.split('-')]
                        for r in field_rules.split(' or ')]
        line = next(file).strip()

    line = next(file).strip()
    line = next(file).strip()
    my_ticket = [int(i) for i in line.split(',')]

    line = next(file).strip()
    line = next(file).strip()
    line = next(file).strip()
    while line:
        other_tickets.append([int(i) for i in line.split(',')])
        try:
            line = next(file).strip()
        except StopIteration:
            line = ''

print(rules)
print(my_ticket)
print(other_tickets)

errors = 0
for t in other_tickets:
    for i in t:
        if not any(r[0] <= i <= r[1] for rr in rules.values() for r in rr):
            errors += i

print('errors:', errors)