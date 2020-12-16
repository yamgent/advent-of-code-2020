# Notes for day 13

## How to solve second part

Take the first example in the question. The question can be reduced to the
following form: what is the value of `x` that satisfies all the following
equations:

```
x = 0 (mod 7)
x + 1 = 0 (mod 13)
x + 4 = 0 (mod 59)
x + 6 = 0 (mod 31)
x + 7 = 0 (mod 19)
```

which can be converted to the following form (**note**: the time interval is
negative, which is also the reason why in `2.py`, we must negate `x[0]` in
our `enumerate`d list):

```
x = 0 (mod 7)
x = -1 (mod 13)
x = -4 (mod 59)
x = -6 (mod 31)
x = -7 (mod 19)
```

This form can be solved using the Chinese Remainder Theorem. The algorithm is
as follows [1]:

Let `m_1`, ..., `m_n` be pairwise coprime (i.e. `gcd(m_i, m_j) = 1` when
`i != j`), then the system of `n` equations:

```
x = a_1 (mod m_1)

   ...

x = a_n (mod m_n)
```

has a unique solution for `x % M`, where `M = m_1, ... m_n`.

To find `x`, define `b_i = M/m_i`, and `b_i' = (b_i)^(-1) (mod m_i)` (which
means that `b_i * b_i' = 1 (mod m_i)`, see "Extended GCD" for details on
how to find this). Then, `x` will be as follows:

`x = sum(a * b * b') % M`

## Extended GCD

If `b_i (mod m_i)` is given, and you want to find the inverse
`b_i' = (b_i)^(-1) (mod m_i)` -> `b_i * b_i' = 1 (mod m_i)`, then you can
solve it using the following equation:

`(b_i * b_i') + (m_i * [whatever]) = 1 = gcd(b_i, m_i)`

This can be found using the extended GCD algorithm. Refer to discrete structure
course notes for extended GCD algorithm, or take the algorithm directly from
Wikipedia [2].

[1] - https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
[2] - https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
