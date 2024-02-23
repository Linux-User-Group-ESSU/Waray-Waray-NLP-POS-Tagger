def load_tagset(filepath):
    import csv
    datas = {}

    with open(filepath, "r") as inFile:
        inFile_data = csv.reader(inFile)
        for i in inFile_data:
            end = len(i)
            for j in range(0, end, 2):
                datas[i[j].lower().strip()] = i[j+1]
    
    return datas