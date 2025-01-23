'''
numbers = []
for elements in range(1, 11):
    numbers.append(elements * 2)

print(numbers)

#              elemento    ciclo donde se extraen elementos
numbers_v2 = [element * 2 for element in range(1,11)]  #list comprehension
print(numbers_v2)
'''

numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)

#             elemento   ciclo extraer   condicion opcional
numbers_v2 = [i*2 for i in range(1,11) if i%2 == 0] #list comprehension
print(numbers_v2)
