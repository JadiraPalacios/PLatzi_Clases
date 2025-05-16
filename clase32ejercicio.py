import json 
file_path="products.json"

new_product={
    "nombre": "Cargador Inalámbrico",
    "precio": "75",
    "cantidad": 100,
    "marca": "MarcaX",
    "categoría": "accesorios",
    "fecha_entrada": "2025-05-12"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path,mode="w") as file:
    json.dump(products, file , indent=4)

