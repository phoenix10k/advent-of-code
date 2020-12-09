from collections import defaultdict

rules = {}
rev_rules = defaultdict(list)


with open('input.txt') as file:
    for line in file:
        rule_col, contents = line.split(" bags contain ")
        contents = [c.split(" bag")[0].split(maxsplit=1) for c in contents.split(", ")]
        for num, col in contents:
            rev_rules[col].append(rule_col)
        rules[rule_col] = contents
print(rules)
print(rev_rules)

count = 0
current = 'shiny gold'

def can_contain(outer_col, inner_col):
    contents = [c[1] for c in rules.get(outer_col, [])]
    if inner_col in contents:
        return True
    return any(can_contain(c, inner_col) for c in contents)

for rule_col, contents in rules.items():
    if can_contain(rule_col, 'shiny gold'):
        count += 1

print("outer colours:", count)


def contains(col):
    count = 1
    for num, in_col in rules[col]:
        if num != 'no':
            print('num:', num, 'col:', in_col)
            num=int(num)
            count += num * contains(in_col)
    return count

print("contains:", contains('shiny gold') - 1)
