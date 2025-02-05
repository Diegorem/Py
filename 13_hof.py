def increment(x):
    return x + 1


def high_order_function(x, func):
    return x + func(x)


print(high_order_function(5, increment))
