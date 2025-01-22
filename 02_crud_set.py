my_set = {'mex', 'col', 'bol'}

size = len(my_set)
print(size)

print('col' in my_set)
print('pe' in my_set)

# add
my_set.add('pe')
print(my_set)
my_set.add('pe')
print(my_set) #no se duplica aunque se agregue 2 veces

#update
my_set.update({'arg','ecua','pe'})
print(my_set)

#remove
#my_set.remove('arg') forma de remover que no es muy óptima
my_set.discard('ar') #no causa error si no existe el elemento en el set
print(my_set)
my_set.discard('arg')
print('borrado ', my_set)

my_set.clear() #Limpia el set
print(my_set)
print(len(my_set))