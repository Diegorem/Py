
price = 100 #Scope global

def increment():
    price = 200 # Scope local
    result = price + 10
    return  result

print(price)
price_2 = increment()
print(price_2)
# print(result) ERROR