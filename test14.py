import copy

a = [1, 2, [3, 4]]
# b = a

b = list(a)

print(b is a)
b[1] = 100
print(a)

b = copy.deepcopy(a)

b[2][0] = 100
print(b)
print(a)