TT_TERMINAL = 0
TT_SUBRULES = 1

def match(rules, active_rule, line, pos):
    if active_rule[0] == TT_TERMINAL:
        return (True, pos + 1) if line[pos] == active_rule[1] else (False, pos)
    elif active_rule[0] == TT_SUBRULES:
        for rule in active_rule[1]:
            full_match = True
            curpos = pos
            for key in rule:
                res, curpos = match(rules, rules[key], line, curpos)
                if not res:
                    full_match = False
                    break
            if full_match:
                return True, curpos
        return False, pos
    else:
        raise Exception()


def follow_rules(rules, line):
    res, pos = match(rules, rules["0"], line, 0)
    if pos != len(line):
        return False
    return res


def main():
    rules = {}
    line = input().strip()
    while line:
        key, values = [x.strip() for x in line.split(':')]
        if values.startswith('"') and values.endswith('"'):
            rules[key] = (TT_TERMINAL, values.replace('"', ''))
        else:
            rules[key] = (TT_SUBRULES, [x.strip().split(' ') for x in values.split('|')])
        line = input().strip()

    count = 0
    try:
        while True:
            line = input().strip()
            count += 1 if follow_rules(rules, line) else 0
    except EOFError:
        pass

    print(count)


main()
