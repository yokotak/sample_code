class ListTranscation:
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, type, value, tb):
        if type is None:
            self.thelist[:] = self.workingcopy
        return False

items = [1, 2, 3]

with ListTranscation(items) as working:
    working.append(4)
    working.append(5)

print(items)

items = [1, 2, 3]

try:
    with ListTranscation(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("We're hosed!")

except RuntimeError:
    pass

print(items)