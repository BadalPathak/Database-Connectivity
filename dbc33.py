import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#16.	Write a query to find the details of employees and with eligibility criteria based on the following: a. If Hire_date is less than or equal to '1999-12-31'then eligible else not eligible
#q ="select * from employees where hire_date<=('1999-12-31');"
q ="select first_name,last_name,hire_date if (hire_date>'1999-12-31','eligible','not eligible')as eligibility_criteria from employees;"
cur.execute(q)
rst = cur.fetchall()
print(rst)
