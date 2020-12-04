import re

REQUIRED = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
HCL_RE = re.compile(r'^#[0-9a-f]{6}$')
ECL_SET = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }
PID_RE = re.compile(r'^\d{9}$')

def val_in_range(val, low, high):
    return val.isdigit() and low <= int(val) <= high


def is_field_valid(key, val):
    if key == 'byr':
        return val_in_range(val, 1920, 2002)
    elif key == 'iyr':
        return val_in_range(val, 2010, 2020)
    elif key == 'eyr':
        return val_in_range(val, 2020, 2030)
    elif key == 'hgt':
        if val.endswith('cm'):
            return val_in_range(val[:-2], 150, 193)
        elif val.endswith('in'):
            return val_in_range(val[:-2], 59, 76)
        else:
            return False
    elif key == 'hcl':
        return HCL_RE.match(val)
    elif key == 'ecl':
        return val in ECL_SET
    elif key == 'pid':
        return PID_RE.match(val)
    else:
        return True


def is_valid(content):
    entries = [ent.split(':') for ent in ' '.join(content).split(' ')]
    present = {ent[0] for ent in entries}

    return REQUIRED <= present and all([is_field_valid(key, val) for key, val in entries])


def main():
    # while True:
    #     key, val = input().split(':')
    #     print(is_field_valid(key, val))

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
