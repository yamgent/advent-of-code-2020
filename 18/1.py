import sys

TT_NUM = 0
TT_PLUS = 1
TT_MUL = 2
TT_OPEN = 3
TT_CLOSE = 4

class Token:
    def __init__(self, token_type, pos, val):
        self.token_type = token_type
        self.pos = pos
        self.val = val

    def __repr__(self):
        return 'Token(token_type={}, pos={}, val="{}")'.format(self.token_type, self.pos, self.val)


def raise_error(line, pos, message):
    print(line)
    print((' ' * pos) + '^')
    print('Error (pos {}): {}'.format(pos, message))
    raise Exception(message)


def lex(line):
    pos = 0
    tokens = []

    def skip_space():
        nonlocal pos
        while pos < len(line) and line[pos] == ' ':
            pos += 1

    while True:
        skip_space()
        if pos >= len(line):
            break

        if line[pos].isnumeric():
            end = pos
            while end < len(line) and line[end].isnumeric():
                end += 1
            tokens.append(Token(TT_NUM, pos, int(line[pos:end])))
            pos = end
        elif line[pos] == '+':
            tokens.append(Token(TT_PLUS, pos, '+'))
            pos += 1
        elif line[pos] == '*':
            tokens.append(Token(TT_MUL, pos, '*'))
            pos += 1
        elif line[pos] == '(':
            tokens.append(Token(TT_OPEN, pos, '('))
            pos += 1
        elif line[pos] == ')':
            tokens.append(Token(TT_CLOSE, pos, ')'))
            pos += 1
        else:
            raise_error(line, pos, 'Invalid symbol {}'.format(line[pos]))

    return tokens


def parse(line, tokens):
    idx = 0

    def fatal(message):
        nonlocal idx
        raise_error(line, tokens[idx].pos, message)

    def is_type(types):
        nonlocal idx
        return tokens[idx].token_type in types

    def must_accept(types, err_message):
        nonlocal idx
        if not is_type(types):
            fatal(err_message)
        val = tokens[idx]
        idx += 1
        return val

    def may_accept(types):
        nonlocal idx
        if not is_type(types):
            return None
        val = tokens[idx]
        idx += 1
        return val

    def has_tokens_left():
        nonlocal idx
        return idx < len(tokens)

    def p_brac_expr():
        must_accept([TT_OPEN], 'Expected "("')
        val = p_expr()
        must_accept([TT_CLOSE], 'Expected ")"')
        return val

    def p_value():
        if is_type([TT_OPEN]):
            return p_brac_expr()
        else:
            return must_accept([TT_NUM], 'Expected number or "("').val

    def p_expr():
        res = p_value()

        while has_tokens_left():
            if may_accept([TT_PLUS]):
                res += p_value()
            elif may_accept([TT_MUL]):
                res *= p_value()
            else:
                break

        return res

    res = p_expr()
    if has_tokens_left():
        fatal('Expected EOF')
    return res


def main():
    total = 0

    for line in sys.stdin:
        line = line.strip()
        tokens = lex(line)
        result = parse(line, tokens)
        total += result

    print(total)


main()
