import time

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print("Hello World")

after(10, greeting)