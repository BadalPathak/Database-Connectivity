import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q4 = "select first_name,last_name from actor;"
cur.execute(q4)
rst = cur.fetchall()
print(rst)
