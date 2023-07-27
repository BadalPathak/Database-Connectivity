import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#12.	Write a query to get the department ID and the total salary payable in each department
q = "select department_id,sum(salary)from employees group by department_id;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
