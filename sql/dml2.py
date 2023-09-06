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
    INSERT INTO fastfood (id, "dateAdded", "dateUpdated", address, categories, city, country, keys, latitude, longitude, name, "postalCode", province, "sourceURLs", websites) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

with open(csv_file_path, 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        row[1] = row[1].replace('T', ' ').replace('Z', '')
        row[2] = row[2].replace('T', ' ').replace('Z', '')
        row[8] = float(row[8])
        row[9] = float(row[9])
        cursor.execute(insert_query, row)
    connection.commit()