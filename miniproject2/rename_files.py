import os
def rename_Files():
	path = "/Users/NarenMudivarthy/Desktop/git/Programming-Foundations-with-Python-Udacity/miniproject2/prank"
	#Gets all files from the given path to dir
	dirs = os.listdir(path)
	#getcwd is to get current working directory
	saved_path = os.getcwd()
	#To change current directory
	os.chdir("/Users/NarenMudivarthy/Desktop/git/Programming-Foundations-with-Python-Udacity/miniproject2/prank")
	for file in dirs:
		#print file
		os.rename(file,file.translate(None,"0123456789"))
		#print file
	os.chdir(saved_path)

rename_Files()