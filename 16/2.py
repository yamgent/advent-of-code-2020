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

    def is_field_candidate(self, tickets, field_index):
        return all(map(lambda ticket: any(map(lambda ran: ran.in_range(ticket[field_index]), self.ranges)), tickets))


def ticket_valid(ticket, fields):
    return all(map(lambda ticket_field: any(map(lambda field: any(map(lambda ran: ran.in_range(ticket_field), field.ranges)), fields)), ticket))


def main():
    # === read inputs ===
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

    # print(fields)
    # print(your_tickets)
    # print(nearby_tickets)

    # === process inputs ===
    nearby_tickets = list(filter(lambda ticket: ticket_valid(ticket, fields), nearby_tickets))
    all_tickets = [your_tickets] + nearby_tickets

    # print(all_tickets)

    correct_fields = [None] * len(fields)
    unpicked_fields = list(fields)
    while not all(map(lambda f: f is not None, correct_fields)):
        # print(correct_fields)

        for i in range(len(correct_fields)):
            if correct_fields[i] is not None:
                continue

            candidate_fields = []
            for field in unpicked_fields:
                if field.is_field_candidate(all_tickets, i):
                    candidate_fields.append(field)

            if len(candidate_fields) == 1:
                correct_fields[i] = candidate_fields[0]
                unpicked_fields = list(filter(lambda f: f.name != correct_fields[i].name, unpicked_fields))
                break

    # print(correct_fields)

    total = 1
    for i in range(len(correct_fields)):
        curr_field = correct_fields[i]
        if curr_field.name.startswith('departure'):
            total *= your_tickets[i]

    print(total)

main()
