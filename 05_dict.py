"""
dict = {}
for i in range(1,6):
    dict[i] = i * 2

print(dict)

dict_v2 = {i: i*2 for i in range(1,6)} # list comprehension
print(dict_v2)
"""

"""
import random
countries = ['col', 'mex', 'bol', 'per']
population = {}
for country in countries:
    population[country] = random.randint(1,5000000)

print(population)

population_v2 = {country: random.randint(1,5000000) for country in countries} # list comprehension
print(population_v2)
"""

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages))) # zip se usa para juntar 2 listas

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
