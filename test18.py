# s = range(3)
# _iter = s.__iter__()
# while True:
#     print(_iter)
#     try:
#         x = _iter.__next__()
#     except StopIteration:
#         break
#     print(x)

class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        x = self.start
        while x < self.stop:
            yield x
            x += self.step

nums = FRange(0.0, 1.0, 0.1)
for x in nums:
    print(x)