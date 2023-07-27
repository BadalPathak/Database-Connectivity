import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#19.	Write a query to find the count of employees hired in each year and sort them  
q = "select count(*),year(hire_date) from employees group by year(hire_date)order by year(hire_date)asc;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
