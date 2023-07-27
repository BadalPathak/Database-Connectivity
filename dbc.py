import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="sakila")
cur = z.cursor()
q1 = "select * from country"
cur.execute(q1)
rst = cur.fetchall()
for i in rst:
    for j in i:
        print(j,end=" ==> ")
    print()

q2 = "show tables;"
cur.execute(q2)
rst = cur.fetchall()
print(rst)