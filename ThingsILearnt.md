# Things I Learnt

## New

- Set comprehension exists in Python: `{int(x) for x in input().split(',')}`
- Dictionary comprehension also exist: `{key: value for key, value in result}`
- Complex number: `4 + 6j` (day 12)
- Chinese Remainder Theorem (day 13)
- List comprehension can have multiple `for` (instead of doing nesting):

  ```python
  [(x, y) for x in range(2) for y in range(4)]

  # result = [(0, 0), (0, 1), (0, 2), ... , (1, 2), (1, 3)]
  ```

- List comprehension can filter also:

  ```python
  [x for x in range(20) if x % 4 != 0]

  # result = [1,2,3,5,6,7, ..., 18,19]
  ```

- List comprehensions are eagerly evaluated, `map`/`filter` are lazily
  evaluated (need `list()`).
- You can do a javascript's `forEach()` with a list comprehension:

  ```python
  [print(x) for x in range(20)]

  # result:
  #   0
  #   1
  #   2
  #   ...
  #   18
  #   19
  ```

- Lists have `.index()` to find index of an element (it doesn't have `.find()`
  like javascript though).
- Lists have `.reversed()`
- Shunting-Yard algorithm (day 18) (alternative algo, not implemented)
- Cocke-Younger-Kasami algorithm (day 19)

## Refreshed

- Python regex: Use `r'...'` so that you don't have to escape regular
  expression.

  ```python
  import re

  pattern = re.compile(r'...')
  # capture all groups, different from group(int) which has 0th element
  # as fully matched strings
  (a, b, c) = pattern.match(line).groups()
  ```

- Set subset is `set_a <= set_b` (see docs for other possible operations)
- `all()` and `any()`
- `int('010101', 2)` to convert binary strings to numbers.
- `__repr__` to override what `print()` does to an object.
- Dynamic programming (day 10)
- `enumerate()`
- `dict.items()` returns a `(key, value)` tuple.
