# x = 42
# def func():
#     print(x)
#     x = 13

# print(func())

# class Config:
#     x = 42

#     def func():
#         Config.x = 13

# def countdown(start):
#     n = start

#     def display():
#         print("T-minus", n)

#     while n > 0:
#         display()
#         n -= 1

# countdown(10)

def countdown(start):
    n = start

    def display():
        print("T-minus", n)

    def decrement():
        nonlocal n
        n -= 1

    while n > 0:
        display()
        decrement()

countdown(10)