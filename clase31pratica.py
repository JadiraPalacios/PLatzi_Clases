import csv
file_path = 'products_updated.csv'
updated_file_path = 'products_newfile.csv'

with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    columnasnombres = csv_reader.fieldnames + ['Codigo_producto']

    with open(updated_file_path, 'w', newline='') as nuevofile:
        csv_writer = csv.DictWriter(nuevofile, fieldnames=columnasnombres)
        csv_writer.writeheader()

        for row in csv_reader:
            row['Codigo_producto'] = row['price'][0]
            csv_writer.writerow(row)

