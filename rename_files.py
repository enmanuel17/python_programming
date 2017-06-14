#rename files
#E hernandez
from os import listdir

def rename_files():
	#1 get file names from a folder
	file_list = listdir(r"/home/enmanuel/Downloads/prank/prank/")
	print (file_list)
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None, "0123456789"))
		

rename_files()
