#!/usr/bin/python3
import csv
import nltk
from checker import *
from saver import save_unknown_tags
from tag_file_loader import load_tagset
from read_files import read_files

datas = load_tagset("newTag.csv")
untagged = []
untagged_in_file = []


with open(f"../Untagged_Word/untagged.csv", "r") as untagged_data:
    reader = csv.reader(untagged_data)
    for i in reader:
        untagged_in_file.append(i[0])
#Get all the articles filename

files = read_files("../New_Article")
for dataset_file in files:

    output_file = dataset_file.replace(".txt", ".csv")
    with open(f"../Tagged_Article/{output_file}", "w") as tagged_file:
        tagged_writer = csv.writer(tagged_file)
        with open(f"../New_Article/{dataset_file}", "r") as dataset:
            reader = dataset.readlines()
            counter = 0
            for i in reader:
                #skip the author and published by
                if counter >= 1 and counter <= 3: pass
                else:
                    i = i.strip("\n")
                    token = nltk.word_tokenize(i)
                    tagged = []
                    for j in token:
                        if is_special(j):
                            tagged.append(f"{j}|?")
                        else:
                            word = j.lower().strip().replace(".", "").replace(",", "")
                            if word in datas:
                                tagged.append(f"{word}|{datas[word]}")
                            elif is_int(word):
                                tagged.append(f"{word}|NMBR")
                            else:
                                tagged.append(f"{word}|OOV")
                                if word not in untagged:
                                    untagged.append(word)
                    
                    tagged_writer.writerow(tagged)
                counter += 1



#Save unknown tags
save_unknown_tags(
    filepath="../Untagged_Word/untagged.csv",
    untagged=untagged,
    untagged_in_file=untagged_in_file
)
