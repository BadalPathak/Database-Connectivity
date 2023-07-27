import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#14.	Write a query to find the details of employees, who got hired very early and got commission percentage. 
#q ="select min(hire_date) from employees;"
#q ="select hire_date from employees group by hire_date;"
#q ="select first_name,hire_date from employees group by first_name,hire_date having min(hire_date);"
q ="select first_name,hire_date from employees where hire_date in('1987-06-17','1989-09-21');"
cur.execute(q)
rst = cur.fetchall()
print(rst)
