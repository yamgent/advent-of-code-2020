REQUIRED = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

def is_valid(content):
    entries = [ent.split(':') for ent in ' '.join(content).split(' ')]
    present = {ent[0] for ent in entries}

    return REQUIRED <= present


def main():
    valid = 0
    content = []

    try:
        while True:
            line = input()
            if line:
                content.append(line)
            else:
                valid += 1 if is_valid(content) else 0
                content.clear()

    except EOFError:
        valid += 1 if is_valid(content) else 0

    print(valid)

main()
