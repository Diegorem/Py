def find_vol(length = 1, width = 1, depth = 1): #Así se previene que haya algun error si no se ponen datos al correr la función
    return length * width * depth, width, 'Hola'

result, width, text = find_vol(width=4)
print(result)
print(width)
print(text)
