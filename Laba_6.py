def cast(tip):
    def func(number):
        def inner(*n):
            answer = number(*n)
            return tip(answer)
        return inner
    return func

@cast(str)
def sum(c, d):
    return c+d
num = sum(10, 5)

print(num)
print(type(num))