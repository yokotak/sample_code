#%%
def countdown(n):
    print("Conting down from", n)
    while n > 0:
        yield n
        n -= 1

# for x in countdown(10):
#     print("T-minus", x)

#%%
c = countdown(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(c.__next__())

#%%
c = countdown(3)
for n in c:
    print("T-minus", n)

# %%
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

# %%
c = Countdown(10)
# %%
for i in c:
    print("T-minus", i)
# %%
def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1

def contdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1

def up_and_down(n):
    yield from countup(n)
    yield from Countdown(n)
# %%
for x in up_and_down(5):
    print(x, end="")
# %%
def up_and_down(n):
    for x in countup(n):
        yield x
    for x in Countdown(n):
        yield x
# %%
def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
# %%
a = [1, 2, [3, [4, 5], 6, 7], 8]
for x in flatten(a):
    print(x, end = " ")

# %%
