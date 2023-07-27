import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q = "select first_name,last_name from actor where last_name='johansson';"
cur.execute(q)
rst = cur.fetchall()
print(rst)
