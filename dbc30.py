import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#14.Write a query to find the details of employees, who got hired very early and got commission percentage.
#q = "select first_name,year(hire_date) from employees group by first_name,year(hire_date)limit 2;"
q = "select min(hire_date) from employees;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
