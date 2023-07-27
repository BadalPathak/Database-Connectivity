import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#10.	Write a query to get the number of employees with the same job 
q = "select job_id,count(*) from employees group by job_id;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
