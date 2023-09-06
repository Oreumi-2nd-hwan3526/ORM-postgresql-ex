import psycopg2
import time

connection = psycopg2.connect(
    host="localhost",
    database="oreumi",
    user="postgres",
    password="1234",
)

cursor = connection.cursor()

insert_query = """
    INSERT INTO student VALUES (%s, %s, %s, %s)
"""

data_insert = []
with open("day1/data.txt", 'r', encoding='utf-8') as f:
    for i in f.read().split("\n"):
        a, b, c, d = i.split(', ')
        data_insert.append((a, b, c, d))

start = time.time()
cursor.executemany(insert_query, data_insert) # bulk insert
connection.commit()
print("데이터 입력 완료!")
end = time.time()
print("(bulk)Elapsed time: " + str(end-start))

start = time.time()
for i in data_insert:
    cursor.execute(insert_query, i) # single insert
connection.commit()
print("데이터 입력 완료!")
end = time.time()
print("(single)Elapsed time: " + str(end-start))

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)