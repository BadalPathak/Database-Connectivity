import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#9.	Find out how many employees are in department 80. 
q = "select * from employees where department_id=80;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
