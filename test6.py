# import time

# def countdown(n):
#     print("Counting down from", n)
#     while n>0:
#         yield n
#         n -= 1

# for n in countdown(10):
#     if n == 1:
#         break
#     # print(n)
#     # time.sleep(1)

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