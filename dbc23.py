import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
q = "select department_id,avg(salary)from employees group by department_id having avg(salary)>8000;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
