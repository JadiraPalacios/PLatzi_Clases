import json

#","r es un modo
#lectura del archivo
with open('products.json', 'r') as file:
    products = json.load(file)

for product in products:
    #print(product)

    print(f"Product:{product["name"]},Price: {product["price"]}")
 