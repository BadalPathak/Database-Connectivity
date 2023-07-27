import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q3 = "desc actor;"
cur.execute(q3)
rst = cur.fetchall()
print(rst)
