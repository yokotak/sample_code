# def func(w, x, y, z):
#     list = []
#     list.append(w)
#     list.append(x)
#     list.append(y)
#     list.append(z)
#     print(list)

# func("hello", 3, z = [1, 2], y = 7)

def read_data(filename, *, debug=False):
    with open(filename) as f:
        print(f)

data=read_data("Data.csv", debug = True)

def product(first, *values, scale=1):
    result = first * scale
    for val in values:
        result = result * val
    return result
    
result = product(2, 3, 4)
print(result)

result = product(2, 3, 4, scale = 10)
print(result)