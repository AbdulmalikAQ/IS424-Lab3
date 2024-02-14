x = int(input("Enter a number of repetitions: "))

def repeat(f):
    def wrapper():
        for _ in range(x):
            f()
    return wrapper

@repeat
def hello():
       print('Hello')

hello()