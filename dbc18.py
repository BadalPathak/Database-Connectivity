import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
q = "select first_name from employees where first_name like '_____h';"
cur.execute(q)
rst = cur.fetchall()
print(rst)
