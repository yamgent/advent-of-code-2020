import re

REQUIRED = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
HCL_RE = re.compile(r'^#[0-9a-f]{6}$')
ECL_SET = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }
PID_RE = re.compile(r'^\d{9}$')

def val_in_range(val, low, high):
    return val.isdigit() and low <= int(val) <= high


def is_field_valid(key, val):
    if key == 'byr':
        if not val_in_range(val, 1920, 2002):
            return False
    elif key == 'iyr':
        if not val_in_range(val, 2010, 2020):
            return False
    elif key == 'eyr':
        if not val_in_range(val, 2020, 2030):
            return False
    elif key == 'hgt':
        if val.endswith('cm'):
            if not val_in_range(val[:-2], 150, 193):
                return False
        elif val.endswith('in'):
            if not val_in_range(val[:-2], 59, 76):
                return False
        else:
            return False
    elif key == 'hcl':
        if not HCL_RE.match(val):
            return False
    elif key == 'ecl':
        if val not in ECL_SET:
            return False
    elif key == 'pid':
        if not PID_RE.match(val):
            return False
    return True


def is_valid(content):
    entries = [ent.split(':') for ent in ' '.join(content).split(' ')]
    present = {ent[0] for ent in entries}

    if not REQUIRED <= present:
        return False

    for key, val in entries:
        if not is_field_valid(key, val):
            return False

    return True


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
