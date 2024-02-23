def read_files(foldername : str) -> list[str]:
    
    from os import listdir
    from os.path import isfile, join

    files = []
    for i in listdir(foldername):
        if isfile(join(foldername, i)):
            files.append(i)
    return files

if __name__ == "__main__":
    read_files("../Tagged_Article")