import sys


class RuleInner:
    def __init__(self, input_inner):
        content = input_inner.strip().split(' ')
        self.name = ' '.join(content[1:])
        self.amount = int(content[0])

    def __repr__(self):
        return 'RuleInner(name="{}", amount={})'.format(self.name, self.amount)


class Rule:
    def __init__(self, input_line):
        line = input_line.replace('bags', '').replace('bag', '').replace('.', '')
        main, inner = [x.strip() for x in line.split('contain')]
        inner = [] if inner == 'no other' else [RuleInner(x.strip()) for x in inner.split(',')]

        self.main = main
        self.inner = inner

    def __repr__(self):
        return 'Rule(main="{}", inner={})'.format(self.main, self.inner)


class GraphEdge:
    def __init__(self, dest, value):
        self.dest = dest
        self.value = value

    def __repr__(self):
        return 'GraphEdge(dest="{}", value="{}")'.format(self.dest, self.value)


class Graph:
    def __init__(self, rules):
        self.ad_list = {}
        for rule in rules:
            for rinner in rule.inner:
                if rinner.name not in self.ad_list:
                    self.ad_list[rinner.name] = []
                self.ad_list[rinner.name].append(GraphEdge(rule.main, rinner.amount))

            if rule.main not in self.ad_list:
                self.ad_list[rule.main] = []

    def dfs_collect_nodes(self, start_name):
        result = set()

        def dfs(name):
            if name in result:
                return
            result.add(name)
            for edge in self.ad_list[name]:
                dfs(edge.dest)

        dfs(start_name)
        return result

    def __repr__(self):
        return 'Graph(ad_list="{}")'.format(self.ad_list)


def main():
    rules = [Rule(x) for x in sys.stdin]
    graph = Graph(rules)

    # print(rules)
    # print(graph)

    # subtract ourselves
    total_outer = len(graph.dfs_collect_nodes('shiny gold')) - 1
    print(total_outer)


main()
