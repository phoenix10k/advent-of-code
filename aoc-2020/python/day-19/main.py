rules = {}
messages = []


def parse_tok(token):
    if token[0] == '"':
        return token.strip('"')
    if token == '|':
        return '|'
    return int(token)


with open('input.txt') as file:
    line = next(file).strip()
    while line:
        rule, rule_str = line.split(': ')
        rules[int(rule)] = [[parse_tok(tok) for tok in sub_rule.split()]
                            for sub_rule in rule_str.split(' | ')]
        line = next(file).strip()
    line = next(file).strip()
    while line:
        messages.append(line)
        line = next(file).strip()

print(rules)


def match_rule(rule_num, message):
    rule = rules[rule_num]
    for sub_rule in rule:
        sub_msg = message
        for part in sub_rule:
            if isinstance(part, int):
                match, sub_msg = match_rule(part, sub_msg)
                if not match:
                    break
            elif isinstance(part, str):
                if sub_msg.startswith(part):
                    sub_msg = sub_msg[len(part):]
                else:
                    break
            else:
                raise Exception('Unknown rule')
        else:
            return True, sub_msg

    return False, ''


count = 0
for message in messages:
    match, rest = match_rule(0, message)
    if not match:
        print(message, ": no match")
    elif rest:
        print(message, ": remaining characters", rest)
    else:
        print(message, ": valid")
        count += 1

print("count:", count)
