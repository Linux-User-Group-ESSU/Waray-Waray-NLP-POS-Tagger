def read_files(foldername : str) -> list[str]:
	from os import listdir
	from os.path import isfile, join

	files = []
	try:
		for i in listdir(foldername):
			if isfile(join(foldername, i)) and i.endswith(".csv") :
				files.append(i)
		return files
	except FileNotFoundError:
		print("Warning: Folder Doesn't Exist!")


if __name__ == "__main__":
	read_files("../Tagged_Article")
