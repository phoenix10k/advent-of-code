import itertools
import operator

def calc(tokens):
    tok_itr = 0
    acc = 0
    op = operator.add
    while tok_itr < len(tokens):
        if tokens[tok_itr] == '(':
            lhs, calc_itr = calc(tokens[tok_itr+1:])
        else:
            lhs = int(tokens[tok_itr])
            calc_itr = 0
        acc = op(acc, lhs)
        tok_itr += calc_itr + 1
        
        if tok_itr == len(tokens):
            return acc, tok_itr

        if tokens[tok_itr] == ')':
            return acc, tok_itr + 1

        if tokens[tok_itr] == '+':
            op = operator.add
            tok_itr += 1

        if tokens[tok_itr] == '*':
            rhs, calc_itr = calc(tokens[tok_itr+1:])
            return acc * rhs, tok_itr + calc_itr + 1

    return acc, tok_itr

total = 0
with open('input.txt') as file:
    for line in file:
        tokens = line.split()
        tokens = itertools.chain.from_iterable('('.join(t.split('(')) for t in tokens)
        tokens = [t for t in itertools.chain.from_iterable(')'.join(t.split(')')) for t in tokens) if t]
        result, tok_itr = calc(tokens)
        assert tok_itr == len(tokens)

        print(line.strip(), '=', result)
        total += result

print('total = ', total)
