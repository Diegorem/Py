def increment(x):
    return x + 1


increment_v2 = lambda x : x+1

def high_order_function(x, func):
    return x + func(x)


high_order_function_v2 = lambda x, func: x + func(x)

print(high_order_function(5, increment))

print(high_order_function_v2(5,increment_v2))