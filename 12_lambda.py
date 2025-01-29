def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, lastname : f'Full name is {name.title()} {lastname.title()}'

text = full_name('diego', 'rodriguez')
print(text)
