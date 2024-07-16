# def sumn(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sumn(n-1)

# print(sumn(10))

# a = lambda x, y: x + y
# r = a(2, 3)

# print(r)

x = 2
f = lambda y: x * y
x = 3
g = lambda y, x=x: x * y

print(f(10))
print(g(10))