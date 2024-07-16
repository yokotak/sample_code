# def square(items):
#     for i, x in enumerate(items):
#         # print(i, x)
#         items[i] = x * x
#         # print(items[i])
#     return items

# a = [1, 2, 3, 4, 5]
# calc = square(a)

# print(a)
# print(calc)

# def sum_squares(items):
#     items = [x * x for x in items]
#     return sum(items)

# a = [1, 2, 3, 4, 5]
# result = sum_squares(a)
# print(a)
# print(result)

# items = [10, 8, 6, 4, 2]
# items.sort()
# print(items)

from typing import NamedTuple

class ParseResult(NamedTuple):
    name : str
    value : str

# def parse_value(text):
#     """
#     name=val形式の文字列を(name, val)に分割する
#     """
#     parts = text.split("=", 1)
#     return ParseResult(parts[0].strip(), parts[1].strip())

# name, value = parse_value("url=https://www.python.org")

# print(name, value)

# r = parse_value("url=https://www.python.org")
# print(r.name, r.value)

def parse_value(text):
    parts = text.split("=", 1)
    if len(parts) == 2:
        return ParseResult(parts[0].split(), parts[1].split())
    else:
        raise ValueError("Bad Value")

if result := parse_value("url=https://www.python.org"):
    name, value = result

print(name, value)
