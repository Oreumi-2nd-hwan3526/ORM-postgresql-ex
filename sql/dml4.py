import psycopg2

conn = psycopg2.connect(
    host="private-domain.hash-string.ap-northeast-2.rds.amazonaws.com",
    database="oreumipostgresql",
    user="admin",
    password="12345678",
    )

cur = conn.cursor()
select_query =""" """

# The earlist open date of restaurant in NY province
# """
#     SELECT "dateAdded" FROM fastfood_restaurant_us WHERE province LIKE 'NY' ORDER BY "dateAdded" ASC LIMIT 1
# """

# The number of resturant in NY province
# """
#     SELECT COUNT(*) FROM fastfood_restaurant_us WHERE province LIKE 'NY'
# """

# The number of resturant named McDonald
# """
#     SELECT COUNT(*) FROM fastfood_restaurant_us WHERE name LIKE '%McDonald%'
# """

cur.execute(select_query)
row = cur.fetchone()
print(row)

insert_query = """
    INSERT INTO oreumi_answer (name, answer, question) VALUES (%s, %s, %s)
"""

cur.execute(insert_query, ("홍길동", row[0], "3"))
conn.commit()
conn.close()
