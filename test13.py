import sys

a = -37
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))

c = -37
print(sys.getrefcount(a))

del b
print(sys.getrefcount(a))