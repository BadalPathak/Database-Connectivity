import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
q = "select replace(first_name,'a','A')from employees;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
