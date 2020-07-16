'''
Find all files in subdirectories recursively. A bit dumb but just a practice of writing recursive stuff
July 16th 2020
'''
import os

my_path = "C:\\Users\\hosse\\Desktop"

def all_filenames(my_path):
	for folderName, subfolders, filenames in list(os.walk(my_path)):
		print('Files in ' + folderName + ':')
		for file in filenames:
			print(os.path.join(folderName,file))
		print("")


def all_filenames_recursive(my_path):

	for folderName, subfolders, filenames in list(os.walk(my_path))[:1]:
		print('Files in ' + folderName + ':')
		for file in filenames:
			print(os.path.join(folderName,file))
		print("")
		if subfolders:
			for subfolder in subfolders:
				all_filenames_recursive(os.path.join(folderName,subfolder))
				
				
if __name__ == "__main__":
	print("non-Recursive version (Reference)")
	all_filenames(my_path)	
	print("Recursive version")
	all_filenames_recursive(my_path)