import random
countries = ['col', 'mex', 'bol', 'per']

population_v2 = {country: random.randint(1,5000000) for country in countries} # list comprehension
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 2000000}
print(result)

text = 'Hola, soy Diego'
unique = { caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
print(unique)
