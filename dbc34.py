import mysql.connector as mc
z = mc.connect(host="localhost",port=3308,user="root",password="root",database="hr")
cur = z.cursor()
#17.	Write a query to assign tax slabs based on the following criteria: 
#a. If salary less than or equal to 5000 then ‘Tax slab A’ 
#b. If salary greater than 5000 and less than or equal to 10000 then ‘Tax slab B’ 
#c. If salary greater than 10000 and less than or equal to 15000 then ‘Tax slab C’ 
#d. Else ‘Tax slab C’
q = "select first_name,last_name,hire_date,salary,
	case 
	when salary<=5000 then "TAX SLAB - A"
	when salary>5000 and salary<=10000 then "TAX SLAB - B"
	when salary>10000 or salary<=15000 then "TAX SLAB - C"
    end as 'eligibility criteria'
    from employees;"

cur.execute(q)
rst = cur.fetchall()
print(rst)
