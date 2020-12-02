import re
import sys

def main():
    pattern = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')
    count = 0

    for line in sys.stdin:
        (low, high, letter, pwd) = pattern.match(line).groups()
        if int(low) <= pwd.count(letter) <= int(high):
            count += 1

    print(count)

main()
