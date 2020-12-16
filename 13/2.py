from functools import reduce

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return (int(old_r), int(old_s), int(old_t))


def crt(buses):
    a = list(map(lambda bus: bus[0], buses))
    m = list(map(lambda bus: bus[1], buses))
    M = reduce(lambda acc, m_val: acc * m_val, m)
    b = list(map(lambda m_val: M // m_val, m))
    bp = list(map(lambda i: extended_gcd(b[i], m[i])[1], range(len(buses))))
    x = sum([a[i] * b[i] * bp[i] for i in range(len(buses))]) % M
    return x


def main():
    depart = int(input())
    # NOTE: time interval must be negative due to how the final equation
    # is designed in order to apply CRT. Refer to NOTE.md for more details
    buses = [(-x[0], x[1]) for x in enumerate([int(x) if x != 'x' else 0 for x in input().split(',')]) if x[1] != 0]
    print(crt(buses))


main()
