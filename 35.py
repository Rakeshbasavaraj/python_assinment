import mysql.connector
global con,cursor
import sys
con =mysql.connector.connect(host="localhost",user="root",db="student" )
def connection():
	if con.is_connected():
		print("Connected")
		return True
		
	else:
		print("Not Connected")
		return False
def createdatabase():
	if connection():
		mycursor=con.cursor()
		mycursor.execute("CREATE DATABASE student")
		print("Database is created sucessfully")
	else:
		print("Couldn't connect to mysql server")
def createtable():
	db_con=mysql.connector.connect(host="localhost",db="student",user="root")
	if db_con.is_connected():
		mycursor=db_con.cursor()
		
		mycursor.execute("CREATE TABLE info(sid INT(10) PRIMARY KEY, name VARCHAR(255), branch VARCHAR(255),place VARCHAR(122))")
		
		print("Table student table  is created sucessfully\n")
	else:
		print("Couldn't connect to mysql server")
def insert():
	db_con=mysql.connector.connect(host="localhost",db="student",user="root")
	if db_con.is_connected():
		mycursor=db_con.cursor()
		q = "INSERT INTO info(sid, name, branch,place) VALUES (%s,%s,%s,%s) "
		sid = input("\n Enter your sid\n")
		name = input("\n Enter name\n")
		branch= input("\n Enter your branch \n")
		place=input("\n Enter place\n")
		value=(sid,name,branch,place)
		mycursor.execute(q,value)
		db_con.commit()
		print("Table student table  is created sucessfully\n")
	else:
		print("Couldn't connect to mysql server")
def display():
	db_con=mysql.connector.connect(host="localhost",db="student",user="root")
	if db_con.is_connected():
		mycursor= db_con.cursor()
		query="SELECT * FROM info"
		mycursor.execute(query)
		result=mycursor.fetchall()
		for x in result:
			print(x)
		
	else:
		print("Couldn't connect to mysql server")
	con.close()
def update():
	db_con=mysql.connector.connect(host="localhost",db="student",user="root")
	if db_con.is_connected():
		mycursor= db_con.cursor()
		q=("update info set name=%s WHERE sid =%s") 
		sid = input("\n Enter your name\n")
		name = input("\n Enter sid\n")
		value=(sid,name)
		mycursor.execute(q,value)
		db_con.commit()
		print("Table student table  update sucessfully\n")
	else:
		print("Couldn't connect to mysql server")



def main():
	while True:
		print("1-to create datbase")
		print("2-to create table")
		print("3-to insert value of student")
		print("4-to display the value of student")
		print("5-to display the value of student")
		choice = input("Enter your choice :\t")
		if choice=='1':
			createdatabase()
		if choice=='2':
			createtable()
		if choice=='3':
			insert()
		if choice=='4':
			display()
		if choice == '5':
			update()
		if choice == 'q':
			sys.exit()

if __name__ == "__main__":
	main()
