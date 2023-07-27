import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#11.	Write a query to get the difference between the highest and lowest salaries 
q = "select max(salary)-min(salary) as difference from employees;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
