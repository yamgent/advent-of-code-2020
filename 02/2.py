import re
import sys

def main():
    pattern = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')
    count = 0

    for line in sys.stdin:
        (first, second, letter, pwd) = pattern.match(line).groups()
        first = int(first) - 1
        second = int(second) - 1
        if (pwd[first] == letter or pwd[second] == letter) and pwd[first] != pwd[second]:
            count += 1

    print(count)

main()
