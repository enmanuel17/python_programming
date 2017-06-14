#rename files
#E hernandez
import os


def rename_files():
	#1 get file names from a folder
	file_list = os.listdir("/home/enmanuel/Downloads/prank/prank/")
	print (file_list)
	saved_path = os.getcwd() #gets the current dir.
	print("Current Working Directory is"+saved_path)
	os.chdir("/home/enmanuel/Downloads/prank/prank") #changes the current dir for this program
	#(2) for each file, rename filename
	for file_name in file_list:
		print (file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_files()
