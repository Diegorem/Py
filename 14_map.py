from modulefinder import replacePackageMap

numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

def ingredientes(a, b):
  return a + " es a " + b

menu = list(map(ingredientes, ('carne', 'maiz', 'aguacate'), ('molida', 'tacos', 'guacamole')))

print(list(menu))

ingredientess = ('carne', 'maiz', 'aguacate')
ingredientes_2 = ('molida', 'tacos', 'guacamole')
menu = list(map(lambda a, b: a + ' es a ' + b, ingredientess, ingredientes_2)) # con lambda
print(menu)
