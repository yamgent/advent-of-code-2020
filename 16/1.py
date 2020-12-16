import re

FIELD_DECL_RE = re.compile(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Range(start: {}, end: {})'.format(self.start, self.end)

    def in_range(self, number):
        return self.start <= number <= self.end


class FieldDecl:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    def __repr__(self):
        return 'FieldDecl(name: "{}", ranges: {})'.format(self.name, self.ranges)


def main():
    fields = []
    current = input()
    while current != '':
        vals = FIELD_DECL_RE.match(current).groups()
        fields.append(FieldDecl(vals[0], [Range(int(vals[1]), int(vals[2])), Range(int(vals[3]), int(vals[4]))]))
        current = input()

    assert input() == 'your ticket:'
    your_tickets = [int(x) for x in input().split(',')]

    assert input() == ''
    assert input() == 'nearby tickets:'

    nearby_tickets = []
    try:
        while True:
            line = input()
            nearby_tickets.append([int(x) for x in line.split(',')])
    except EOFError:
        pass

    invalid_sum = 0
    for ticket in nearby_tickets:
        for ticket_field in ticket:
            if all(map(lambda field: all(map(lambda ran: not ran.in_range(ticket_field), field.ranges)), fields)):
                invalid_sum += ticket_field

    print(invalid_sum)

main()
