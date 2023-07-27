import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
q = "select first_name,count(*)from employees group by first_name having count(*)>1;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
