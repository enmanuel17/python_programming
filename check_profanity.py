#Enmanuel Hernandez
# Create a profanity checker, it partest a files and checks for bad words.

import urllib #imports a library to manage url objects

#Defining the main function.
def read_text():
	quotes = open("/home/enmanuel/homework/python_programming/movie_quotes.txt") #opening a file for checking and creating an object of it.
	contents_of_file = quotes.read() #reading the contents of the object into into a variable
	print(contents_of_file) #printing the contents of the object to the screen
	quotes.close() #closes the file. it is good practice to always close a file at the end.
	check_profanity(contents_of_file) #Calls function to check for bad words.

#fuction that checks for profanity.
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) #open the url as an option called connection.
	output = connection.read() #store the output of the GET from the URL inside a variable
	#print(output) 			   #print the output of the GET from the URL.
	connection.close()			#close the url object.

	#Displaying diferent statements
	if "true" in output:
			print("Profanity Alert!!")
	elif "false" in output:
			print("This document has not curse words!")
	else:
		print("Could not scan the document properly.")

#calls the main funtion
read_text()