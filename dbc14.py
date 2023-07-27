import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="world")
cur = z.cursor()
q = "select * from city order by name asc limit 10;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
