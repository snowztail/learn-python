# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
def powers_of_two(xs):
    # xs is a generator (delimited by () not []): can only be used once
    for x in xs:
        # yield is a keyword that is used like return, except the function will return a generator.
        yield 2**x


def interleaved(xs):
    for x in xs:
        yield 2**x
        yield x**2


def sequential(xs):
    for x in xs:
        yield 2**x

    for x in xs:
        yield x**2


print("powers of two:")
for x in powers_of_two([2, 4, 3, 2]):
    print(x)


print("interleaved:")
for x in interleaved([2, 4, 3, 2]):
    print(x)


print("sequential:")
for x in sequential([2, 4, 3, 2]):
    print(x)


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i


# when you call the function, the code you have written in the function body does not run. The function only returns the generator object.
# Then, your code will continue from where it left off each time for uses the generator.
mygenerator = create_generator()
for i in mygenerator:
    # The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop.
    # Then, each subsequent call will run another iteration of the loop you have written in the function and return the next value.
    # This will continue until the generator is considered empty, which happens when the function runs without hitting yield.
    print(i)
