import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#15.	Write a query to get the job_id and related employee's id 
q ="select job_id, group_concat(employee_id,'')from employees group by job_id;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
