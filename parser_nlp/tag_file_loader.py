def load_tagset(filepath):
    import csv
    datas = {}

    with open(filepath, "r") as inFile:
        inFile_data = csv.reader(inFile)
        for i in inFile_data:
            if i:
                data = i[0].split("|")
                datas[data[0].lower().strip()] = data[1]
    
    return datas

if __name__=="__main__":
    print(load_tagset("newTag.csv"))