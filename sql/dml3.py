import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "restaurant",
    user = "postgres",
    password = "1234",
    )

cur = conn.cursor()

update_query = """
    UPDATE fastfood
    SET categories = %s
    WHERE city = %s AND categories IN ('Fast food restaurants', 'Fast Food Restaurant')
"""
    # WHERE city = %s AND categories = 'Fast food restaurants' OR categories = 'Fast Food Restaurant'

# """
#     SELECT "dateAdded", name, address FROM fastfood_restaurant_us
#     WHERE "dateAdded" >= '2018-01-01'
#     ORDER BY "dateAdded" ASC LIMIT 5 OFFSET 5
# """
# """
#     SELECT COUNT(*) AS "버거킹 매점수" FROM fastfood_restaurant_us WHERE name = 'Burger King'
# """
# """
#     SELECT province, COUNT(*) FROM fastfood_restaurant_us 
#     WHERE name = 'Burger King'
#     GROUP BY province
# """

cur.execute(update_query, ("Fast Food Restaurant", "Detroit"))
conn.commit()
conn.close()