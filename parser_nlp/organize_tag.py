#!/usr/bin/python3
import csv
import nltk
import os
from checker import *
from saver import save_unknown_tags
from tag_file_loader import load_tagset

datas = load_tagset("dataset1.csv")
untagged = []
untagged_in_file = []

#Get all the articles filename
files = os.listdir("../New_Article")
for dataset_file in files:
    with open(f"../Untagged_Word/untagged.csv", "r") as untagged_data:
        reader = csv.reader(untagged_data)
        for i in reader:
            untagged_in_file.append(i[0])

    output_file = dataset_file.replace(".txt", "")
    with open(f"../Tagged_Article/{output_file}.csv", "w") as tagged_file:
        tagged_writer = csv.writer(tagged_file)
        with open(f"../New_Article/{dataset_file}", "r") as dataset:
            reader = dataset.readlines()
            counter = 0
            for i in reader:
                #skip the author and published by
                if counter >= 1 and counter <= 3: pass
                else:
                    # lines += 1
                    i = i.strip("\n")
                    token = nltk.word_tokenize(i)
                    tagged = []
                    for j in token:
                        # if "." in j : lines += 1
                        if is_special(j):
                            tagged.append(f"{j}|?")
                        else:
                            word = j.lower().strip().replace(".", "").replace(",", "")
                            if word in datas:
                                tagged.append(f"{word}|{datas[word]}")
                            elif is_int(word):
                                tagged.append(f"{word}|NMBR")
                            else:
                                tagged.append(f"{word}|XX")
                                if word not in untagged:
                                    untagged.append(word)
                    
                    tagged_writer.writerow(tagged)
                counter += 1

    with open("../Tagged_Article/DataTag.csv", "w") as tag_write:
        with open("dataset1.csv", "r") as tag_file:
                tag_reader = csv.reader(tag_file)
                tagged = []
                for ii in tag_reader:
                    end = len(ii)
                    for jj in range(0, end, 2):
                        if ii[jj].strip():
                            tag_write.writelines(f"{ii[jj].strip()}|{ii[jj+1].strip()}\n")




#Save unknown tags
save_unknown_tags(
    filepath="../Untagged_Word/untagged.csv",
    untagged=untagged,
    untagged_in_file=untagged_in_file
)
