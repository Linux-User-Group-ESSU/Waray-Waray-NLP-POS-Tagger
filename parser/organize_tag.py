#!/usr/bin/python3
import csv
import nltk
import re
import os

def is_special(string):
	pattern = re.compile(r"^[^\w\s]+$")
	return bool(re.match(pattern, string))

def is_int(param):
    try:
        int(param)
        return True
    except:
        return False

datas = {}
with open("dataset1.csv", "r") as inFile:
    inFile_data = csv.reader(inFile)
    for i in inFile_data:
        end = len(i)
        for j in range(0, end, 2):
            datas[i[j].lower().strip()] = i[j+1]
# lines = 0
untagged = []
untagged_in_file = []

files = os.listdir("../SHIN/articles")
for dataset_file in files:
    with open(f"../Untagged_Word/untagged.csv", "r") as untagged_data:
        reader = csv.reader(untagged_data)
        for i in reader:
            untagged_in_file.append(i[0])

    output_file = dataset_file.replace(".txt", "")
    with open(f"../Tagged_Article/{output_file}.csv", "w") as tagged_file:
        tagged_writer = csv.writer(tagged_file)
        with open(f"../SHIN/articles/{dataset_file}", "r") as dataset:
            reader = dataset.readlines()
            counter = 0
            for i in reader:
                if counter != 1 or counter != 2:
                    print(counter)
                    # lines += 1
                    i = i.strip("\n")
                    token = nltk.word_tokenize(i)
                    tagged = {}
                    for j in token:
                        # if "." in j : lines += 1
                        if is_special(j): pass
                        else:
                            word = j.lower().strip().replace(".", "").replace(",", "")
                            if word in datas:
                                tagged[word] = datas[word]
                            elif is_int(word):
                                tagged[word] = "NMBR"
                            else:
                                tagged[word] = "FX"
                                if word not in untagged:
                                    untagged.append(word)
                    
                    flat_data = data_list = [item for pair in tagged.items() for item in pair]
                    tagged_writer.writerow(flat_data)
                counter += 1

print(tagged)
# print(lines)

with open("../Untagged_Word/untagged.csv", "a") as untagged_file:
    untagged_writer = csv.writer(untagged_file)
    for i in untagged:
        if i not in untagged_in_file:
            untagged_writer.writerow([i])
