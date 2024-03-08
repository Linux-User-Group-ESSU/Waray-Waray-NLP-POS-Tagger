import csv
from tag_file_loader import load_tagset
from read_files import read_files
from string import punctuation
from checker import is_int

datas = load_tagset("newTag.csv")
punctuations = list(set(punctuation))

files = read_files("../Tagged_Article_Corrected")
for file in files:
    updated_sentence = []
    with open(f"../Tagged_Article_Corrected/{file}", "r") as dataset:
        reader =  csv.reader(dataset)
        for i in reader:
            sentence = []
            for j in i:
                word = j.split("|")[0]
                tag = j.split("|")[1].strip(" ").strip("\n")

                if tag == "OOV":
                    if word in punctuations:
                        sentence.append(f"{word}|?")
                    elif word.lower().strip() in datas:
                        sentence.append(f"{word}|{datas[word]}")
                    elif is_int(j):
                        sentence.append(f"{j}|NMBR")
                    else:
                        sentence.append(f"{word}|OOV")
                else:
                    sentence.append(f"{word}|{tag}")
            
            updated_sentence.append(sentence)
        
    with open(f"../Tagged_Article/{file}", "w") as newWrite:
        writer = csv.writer(newWrite)

        for i in updated_sentence:
            writer.writerow(i)