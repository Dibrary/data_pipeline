import psycopg2 as db
conn_string="dbname='dataengineering' host=192.168.0.121 user='postgres' password='비밀번호'"

conn = db.connect(conn_string)

cur = conn.cursor()

query = "select * from users"


cur.execute(query)

for record in cur:
    print(record)