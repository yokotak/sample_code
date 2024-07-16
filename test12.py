# def compare(a, b):
#     if a is b:
#         print("same object")

#     if a == b:
#         print("same value")

#     if type(a) is type(b):
#         print("same type")

# a = [1, 2, 3]
# b = [1, 2, 3]

# compare(a, a)

# compare(a, b)

# compare(a, [4, 5, 6])

# items = list()

# if isinstance(items, list):
#     items.append(item)

# def removeall(items: list, item)->list:
#     return[i for i in items if i != item]

class mylist(list):
    def removeall(self, val):
        return [i for i in self if i != val]

items = mylist([5, 8, 2, 7, 2, 13, 9])
x = items.removeall(2)
print(x)

if isinstance(items, (list, tuple)):
    maxval = max(items)

print(maxval)
