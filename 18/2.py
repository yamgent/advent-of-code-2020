import sys

TT_ERROR = -1
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


def do_error(line, token):
    print(line)
    print((' ' * (token.pos)) + '^')
    print('Error (pos {}): {}'.format(token.pos, token.val))
    raise Exception(token.val)


def lex(line):
    pos = 0
    tokens = []
    while True:
        while pos < len(line) and line[pos] == ' ':
            pos += 1
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
            do_error(line, Token(TT_ERROR, pos, 'Cannot understand symbol {}'.format(line[pos])))

    return tokens


def p_brac(line, tokens, i):
    val, i = p_stat(line, tokens, i)
    if tokens[i].token_type != TT_CLOSE:
        do_error(line, Token(TT_ERROR, tokens[i].pos, 'Expected ")"'))
    return val, i + 1


def p_val(line, tokens, i):
    if tokens[i].token_type == TT_OPEN:
        return p_brac(line, tokens, i + 1)
    elif tokens[i].token_type == TT_NUM:
        return tokens[i].val, i + 1
    do_error(line, Token(TT_ERROR, tokens[i].pos, 'Expected number or "("'))


def p_plus(line, tokens, i):
    if tokens[i].token_type == TT_PLUS:
        return tokens[i], i + 1
    return Token(TT_ERROR, tokens[i].pos, 'Expected "+"'), i


def p_plus_stat(line, tokens, i):
    lhs, i = p_val(line, tokens, i)

    while i < len(tokens):
        op_token, i = p_plus(line, tokens, i)

        if op_token.token_type == TT_ERROR:
            break

        op = op_token.token_type
        rhs, i = p_val(line, tokens, i)

        lhs += rhs

    return lhs, i


def p_mul(line, tokens, i):
    if tokens[i].token_type == TT_MUL:
        return tokens[i], i + 1
    return Token(TT_ERROR, tokens[i].pos, 'Expected "*"'), i


def p_stat(line, tokens, i):
    lhs, i = p_plus_stat(line, tokens, i)

    while i < len(tokens):
        op_token, i = p_mul(line, tokens, i)

        if op_token.token_type == TT_ERROR:
            break

        op = op_token.token_type
        rhs, i = p_plus_stat(line, tokens, i)

        lhs *= rhs

    return lhs, i


def parse(line, tokens):
    ans, pos = p_stat(line, tokens, 0)
    if pos != len(tokens):
        do_error(line, Token(TT_ERROR, pos, 'Expected EOF'))
    return ans


def main():
    total = 0

    for line in sys.stdin:
        line = line.strip()
        tokens = lex(line)
        result = parse(line, tokens)
        total += result

    print(total)


main()
