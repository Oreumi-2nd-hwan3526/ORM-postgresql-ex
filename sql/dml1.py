import psycopg2
import csv

connection = psycopg2.connect(
    host = "localhost",
    database = "restaurant",
    user = "postgres",
    password = "1234",
    )

cursor = connection.cursor()

csv_file_path = 'Fast_Food_Restaurants.csv'

insert_query = """
    INSERT INTO fastfood (id, dateAdded, dateUpdated, address, categories, city, country, keys, latitude, longitude, name, postalCode, province, sourceURLs, websites) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

with open(csv_file_path, 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        cursor.execute(insert_query, row)

connection.commit()