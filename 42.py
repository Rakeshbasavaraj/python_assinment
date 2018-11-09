#42. Read the regno and name in the file, create a dictinary of these data.
import csv
with open('student','r') as csvfile:
	students_reader=csv.reader(csvfile)
	dictionary_form=dict(students_reader)
	print("File Contents in Dictionary format are:\n",dictionary_form)