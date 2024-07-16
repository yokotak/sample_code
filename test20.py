# def make_table(data, **params):
#     fgcolor = params.pop("fgcolor", "black")
#     bgcolor = params.pop("bgcolor", "white")
#     width = params.pop("width", None)
#     border = params.pop("border", 1)
#     borderstyle = params.pop("borderstyle", "grooved")
#     cellpadding = params.pop("cellpadding", 10)

#     if params:
#         raise TypeError(f"Unsupported cofiguration options {list(params)}")

# items = []

# make_table(
#     items,
#     fgcolor="black",
#     bgcolor="white",
#     border=1,
#     borderstyle="grooved",
#     cellpadding=10,
#     width=400
# )

# print(items)

# def factorial(n: int) -> int:
#     result: int = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result

# print(factorial(5.55))

# def square(items):
#     for i, x in enumerate(items):
#         items[i] = x * x

# a = [1, 2, 3, 4, 5]
# print(square(a))

def sum_squares(items):
    items = [x * x for x in items]
    return sum(items)

a = [1, 2, 3, 4, 5]
result = sum_squares(a)
print(a)
