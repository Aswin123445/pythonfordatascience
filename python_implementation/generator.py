#example of generator funtion


def gen():
    yield 1
    yield 2
    yield 3

lisiter=gen()
print(next(lisiter))
print(next(lisiter))
print(next(lisiter))

