import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#13.Write a query to find the manager ID and the first name, last name and salary of the lowest-paid employee for that manager.
q = "select manager_id,first_name,last_name,min(salary) from employees group by manager_id,first_name,last_name order by min(salary);"
cur.execute(q)
rst = cur.fetchall()
print(rst)
