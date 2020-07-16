'''
Find all files in subdirectories recursively
July 16th 2020
'''
import os

my_path = "C:\\Users\\hosse\\Desktop"
subfolder = True
def all_filenames(my_path):
	for folderName, subfolders, filenames in os.walk(my_path):
		print('Files in ' + folderName + ':')
		for file in filenames:
			print(os.path.join(folderName,file))
		print("")
		if subfolders:
			for subfolder in subfolders:
				all_filenames(os.path.join(folderName,subfolder))
				
if __name__ == "__main__":
	all_filenames(my_path)