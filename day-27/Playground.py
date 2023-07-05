def add(*args):
    print(args[1])

    num_sum = 0
    for n in args:
        num_sum += n
    return num_sum


# print(add(3, 5, 6, 7, 34, 5, 7))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
