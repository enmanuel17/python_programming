#Enmanuel Hernandez
# Create a profanity checker, it partest a files and checks for bad words.

#Defining the main function.
def read_text():
	quotes = open("/home/enmanuel/homework/python_programming/movie_quotes.txt") #opening a file for checking and assigning it to a varialbe for later user.
	contents_of_file = quotes.read() #reading the contents of the file into into a variable
	print(contents_of_file) #printing the contents of the file to the screen
	quotes.close() #closes the file. it is good practice to always close a file at the end.

#calls the main funtion
read_text()