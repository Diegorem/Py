set_a = {'mex', 'col', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)  #unión
print(set_c)
print(set_a | set_b)  #unión simbolo

set_c = set_a.intersection(set_b)  #intersección
print(set_c)
print(set_a & set_b)  #intersección simbolo

set_c = set_a.difference(set_b)  #diferencia de a - b
print(set_c)
print(set_a - set_b)  #diferencia simbolo

set_c = set_b.difference(set_a)  #diferencia de b - a
print(set_c)

set_c = set_a.symmetric_difference(set_b)  #diferencia simétrica
print(set_c)
