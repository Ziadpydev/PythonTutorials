import mysql.connector as mc

mydb = mc.connect(host="localhost",user="root",passwd="1234",database="zaid")

mycusrsor=mydb.cursor()

mycusrsor.execute("select * from student")

result=mycusrsor.fetchone()

for i in mycusrsor:
	print(i)


for i in result:
	print(i)