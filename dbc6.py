import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q = "select actor_id,first_name,last_name from actor where first_name='joe';"
cur.execute(q)
rst = cur.fetchall()
print(rst)
