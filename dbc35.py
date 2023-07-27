import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#18.	Write a query to find the hire year of each employees  
q = "select year(hire_date)from employees;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
