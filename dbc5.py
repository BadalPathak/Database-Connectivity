import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q = "select concat(lower(first_name),'',lower(last_name))as actor_name from actor;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
