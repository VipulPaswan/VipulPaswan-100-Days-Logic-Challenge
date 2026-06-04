def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorator
def say_hello():
    print("Hello World")


say_hello()


#----Output------

Before function
Hello World
After function