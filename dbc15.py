import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="world")
cur = z.cursor()
q = "select name,population from city where id in(5,23,432,2021);"
cur.execute(q)
rst = cur.fetchall()
print(rst)
