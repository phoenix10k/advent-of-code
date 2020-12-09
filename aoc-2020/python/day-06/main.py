
with open('input.txt') as file:
    sum = 0
    group = None
    for line in file:
        if line.strip():
            if group is None:
                group = set(line.strip())
            else:
                group = group.intersection(line.strip())
        else:
            print("group:", ''.join(sorted(group)))
            sum += len(group)
            group = None

print("group:", ''.join(sorted(group)))
sum += len(group)

print(sum)