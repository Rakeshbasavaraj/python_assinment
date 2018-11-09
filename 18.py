#program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. import mysql.connector
global con,cursor
import sys
import datetime
con=mysql.connector.connect(host="localhost",user="root")
def connection():
	if con.is_connected():
		return True
		print("true")
	else:
		return False
		print('no yar')
def c_database():
	if connection():
		mycursor=con.cursor()
		mycursor.execute("CREATE DATABASE rollno181041007")
		print("Database is created sucessfully")
	else:
			print("Couldn't connect to mysql server")
def c_table():
	db_con=mysql.connector.connect(host="localhost",db="rollno181041007",user="root",password="root")
	if db_con.is_connected():
		mycursor=db_con.cursor()
		
		mycursor.execute("CREATE TABLE rollno(id INT(10) PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255),dob DATE)")
		print("Table rollno is created sucessfully\n")
	else:
		print("Couldn't connect to mysql server")
def insert_values():
	db_con=mysql.connector.connect(host="localhost",db="rollno181041007",user="root",password="root")
	if db_con.is_connected():
		mycursor= db_con.cursor()

		q = "INSERT INTO rollno(id, firstname, lastname,dob) VALUES (%s,%s,%s,%s) "
		id = input("\n Enter your id\n")
		firstname = input("\n Enter your first name\n")
		lastname = input("\n Enter your last name\n")
		dob=input("\n Enter date of birth (yyyy/mm/dd)\n")
		value=(id,firstname,lastname,dob)
		mycursor.execute(q,value)
		db_con.commit()
		print("sucessfully inserted")

		if not validate(dob):
			print("Incorrect format.Enter in yyyy/mm/dd format ")
			sys.exit()
	db_con.close()


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def display_values():
	con=mysql.connector.connect(host="localhost",db="rollno181041007",user="root",password="root")
	if con.is_connected():
		mycursor= con.cursor()

		query="SELECT * FROM rollno"

		mycursor.execute(query)
		result=mycursor.fetchall()
		for x in result:
			print(x)
		
	else:
		print("Couldn't connect to mysql server")
	con.close()


def alter_table():
	db_con=mysql.connector.connect(host="localhost",db="rollno181041007",user="root",password="root")
	if db_con.is_connected():
		mycursor= db_con.cursor()

		column=input("Enter column name")
		query = "ALTER TABLE rollno add %s VARCHAR(255)" %(column)
		mycursor.execute(query)
		db_con.commit
		print("sucessfully added the column")
	else:
			print("Couldn't connect to mysql server")
	db_con.close()

def truncate_table():
	con=mysql.connector.connect(host="localhost",db="reg_181041007",user="root",password="root")
	if con.is_connected():
		mycursor= con.cursor()

		query = "DROP TABLE rollno"
		mycursor.execute(query)
		con.commit()
		print("Table is sucessfully dropped")
		
	else:
		print("Couldn't connect to mysql server")
	con.close()

	


def main():
	while True:
		print("Enter your option:\n")
		choice = input("Enter the option :\t")
		if choice=='1':
			c_database()
		if choice=='2':
			c_table()
		if choice=='3':
			insert_values()
		if choice=='4':
			display_values()
		if choice == '5':
			alter_table()
		if choice == '6':
			truncate_table()
		if choice == 'q':
			sys.exit()




if __name__ == "__main__":
	main()