# items = {
#     "number": 42,
#     "text": "Hello World"
# }

# import math
# items["func"] = abs
# items["mod"] = math
# items["error"] = ValueError
# nums = [1, 2, 3, 4]
# items["append"] = nums.append

# print(items["func"](-45))

# print(items["mod"].sqrt(4))

# try:
#     x = int("a lot")
# except items["error"] as e:
#     print("Couldn't convert")

# items["append"](100)
# items["append"](200)

# print(nums)

# print(items)

line = "ACME,100,490.10"
column_types = [str, int, float]
parts = line.split(",")
row = [ty(val) for ty, val in zip(column_types, parts)]
print(row)