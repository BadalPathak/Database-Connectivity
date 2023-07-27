import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#8.	Write a sql query to fetch the details of an employee-Generate another as commission percentage column. And wherever there are null values in this column, convert it to 0.  (HINT : use coalesce() function)
q = "select coalesce(commission_pct,'0')from employees; "
cur.execute(q)
rst = cur.fetchall()
print(rst)
