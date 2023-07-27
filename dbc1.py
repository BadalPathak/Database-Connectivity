import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q2 = "show tables;"
cur.execute(q2)
rst = cur.fetchall()
print(rst)
